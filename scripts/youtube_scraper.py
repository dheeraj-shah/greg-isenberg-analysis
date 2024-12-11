from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os

def scrape_videos():
    driver = webdriver.Chrome()
    try:
        driver.get('https://www.youtube.com/@GregIsenberg/videos')
        wait = WebDriverWait(driver, 10)
        videos = wait.until(EC.presence_of_all_elements_located((By.ID, 'video-title')))
        
        video_data = [{
            'title': video.get_attribute('title'),
            'url': video.get_attribute('href'),
            'video_id': video.get_attribute('href').split('v=')[1],
            'date': 'pending'  # Will be extracted from video page
        } for video in videos if video.get_attribute('href')]
        
        return video_data
    finally:
        driver.quit()

def save_videos(videos):
    with open('videos/latest_videos.json', 'w') as f:
        json.dump(videos, f, indent=2)

if __name__ == '__main__':
    videos = scrape_videos()
    save_videos(videos)