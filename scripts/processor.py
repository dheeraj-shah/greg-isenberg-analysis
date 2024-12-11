import os
import json
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi

class VideoProcessor:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    def process_video(self, video_id, title):
        year = datetime.now().strftime('%Y')
        
        # Get transcript
        transcript = self.get_transcript(video_id)
        
        # Create files
        transcript_path = f'transcripts/{year}/{video_id}.md'
        analysis_path = f'analysis/{year}/{video_id}-analysis.md'
        
        self.create_transcript_file(transcript_path, title, transcript)
        self.create_analysis_file(analysis_path, title, transcript)
        
        return {
            'transcriptPath': transcript_path,
            'analysisPath': analysis_path
        }
    
    def get_transcript(self, video_id):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            return ' '.join(t['text'] for t in transcript)
        except Exception as e:
            print(f'Error getting transcript for {video_id}: {str(e)}')
            return None
    
    def create_transcript_file(self, path, title, content):
        full_path = os.path.join(self.base_path, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        with open(full_path, 'w') as f:
            f.write(f'# {title}\n\n{content}')
    
    def create_analysis_file(self, path, title, transcript):
        full_path = os.path.join(self.base_path, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        analysis = self.analyze_content(transcript)
        
        with open(full_path, 'w') as f:
            f.write(f'''
# Analysis: {title}

## Content Type
{analysis['type']}

## Key Points
{analysis['points']}

## Business Insights
{analysis['insights']}

## Technical Details
{analysis['technical']}

## Distribution Tactics
{analysis['distribution']}
''')
    
    def analyze_content(self, transcript):
        # Basic analysis structure
        return {
            'type': 'Tutorial/Strategy',
            'points': '- Key points from transcript',
            'insights': '- Business insights extracted',
            'technical': '- Technical details noted',
            'distribution': '- Distribution tactics identified'
        }