import json
from youtube_transcript_api import YouTubeTranscriptApi
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from datetime import datetime

class VideoProcessor:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))
    
    def process_transcript(self, video_id):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            text = ' '.join([t['text'] for t in transcript])
            return self.analyze_content(text)
        except Exception as e:
            print(f"Error processing video {video_id}: {str(e)}")
            return None
    
    def analyze_content(self, text):
        sentences = sent_tokenize(text)
        words = word_tokenize(text.lower())
        words = [w for w in words if w not in self.stop_words]
        
        return {
            'word_count': len(words),
            'sentence_count': len(sentences),
            'key_phrases': self.extract_key_phrases(words),
            'topics': self.identify_topics(text)
        }
    
    def extract_key_phrases(self, words):
        # Basic phrase extraction
        phrases = []
        for i in range(len(words)-1):
            if words[i] not in self.stop_words:
                phrases.append(f"{words[i]} {words[i+1]}")
        return phrases[:10]
    
    def identify_topics(self, text):
        topics = []
        business_keywords = ['startup', 'business', 'marketing', 'revenue']
        tech_keywords = ['AI', 'technology', 'software', 'platform']
        
        for keyword in business_keywords + tech_keywords:
            if keyword.lower() in text.lower():
                topics.append(keyword)
        
        return topics

def main():
    processor = VideoProcessor()
    
    with open('videos/latest_videos.json', 'r') as f:
        videos = json.load(f)
    
    for video in videos:
        if not video.get('processed'):
            analysis = processor.process_transcript(video['video_id'])
            if analysis:
                video['analysis'] = analysis
                video['processed'] = True
                video['processed_date'] = datetime.now().isoformat()
    
    with open('videos/processed_videos.json', 'w') as f:
        json.dump(videos, f, indent=2)

if __name__ == '__main__':
    main()