import json
from youtube_transcript_api import YouTubeTranscriptApi
from datetime import datetime
import os

def load_pending_videos():
    with open('data/pending-videos.json', 'r') as f:
        return json.load(f)

def load_completed_videos():
    with open('data/completed-videos.json', 'r') as f:
        return json.load(f)

def process_video(video):
    try:
        video_id = video['url'].split('v=')[1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Create transcript and analysis files
        create_transcript(video, transcript)
        create_analysis(video)
        
        # Move to completed list
        move_to_completed(video, video_id)
        
        return True
    except Exception as e:
        print(f"Error processing {video['title']}: {str(e)}")
        return False

def main():
    pending = load_pending_videos()
    completed = load_completed_videos()
    
    for video in pending['pendingVideos']:
        if process_video(video):
            # Update lists
            pending['pendingVideos'].remove(video)
    
    # Save updated lists
    save_lists(pending, completed)

if __name__ == '__main__':
    main()