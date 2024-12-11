import json
from collections import Counter
from datetime import datetime

def analyze_patterns():
    with open('videos/processed_videos.json', 'r') as f:
        videos = json.load(f)
    
    # Collect patterns
    topics = []
    phrases = []
    for video in videos:
        if video.get('analysis'):
            topics.extend(video['analysis']['topics'])
            phrases.extend(video['analysis']['key_phrases'])
    
    patterns = {
        'common_topics': Counter(topics).most_common(5),
        'recurring_phrases': Counter(phrases).most_common(5),
        'analysis_date': datetime.now().isoformat()
    }
    
    with open('trends/pattern_analysis.json', 'w') as f:
        json.dump(patterns, f, indent=2)

if __name__ == '__main__':
    analyze_patterns()