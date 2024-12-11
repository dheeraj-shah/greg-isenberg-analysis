const puppeteer = require('puppeteer');

async function scrapeVideos() {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://www.youtube.com/@GregIsenberg/videos');
  
  // Wait for video content
  await page.waitForSelector('#video-title');
  
  // Scroll to load more videos
  await autoScroll(page);

  const videos = await page.evaluate(() => {
    const items = document.querySelectorAll('ytd-grid-video-renderer');
    return Array.from(items, item => ({
      title: item.querySelector('#video-title').innerText,
      url: item.querySelector('#video-title').href,
      date: item.querySelector('#metadata-line span:last-child').innerText,
      views: item.querySelector('#metadata-line span:first-child').innerText
    }));
  });

  await browser.close();
  return videos;
}

async function autoScroll(page) {
  await page.evaluate(async () => {
    await new Promise(resolve => {
      let totalHeight = 0;
      const distance = 100;
      const timer = setInterval(() => {
        window.scrollBy(0, distance);
        totalHeight += distance;
        if(totalHeight >= document.body.scrollHeight) {
          clearInterval(timer);
          resolve();
        }
      }, 100);
    });
  });
}

module.exports = { scrapeVideos };