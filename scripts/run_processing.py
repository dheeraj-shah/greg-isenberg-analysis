from processor import VideoProcessor
import json
import os

def main():
    # Load pending videos
    with open('data/pending-videos.json', 'r') as f:
        pending = json.load(f)
    
    processor = VideoProcessor()
    
    for video in pending['pendingVideos']:
        video_id = video['url'].split('v=')[1]
        results = processor.process_video(video_id, video['title'])
        
        if results:
            # Move to completed
            with open('data/completed-videos.json', 'r') as f:
                completed = json.load(f)
            
            completed['completedVideos'].append({
                'title': video['title'],
                'videoId': video_id,
                'date': video['date'],
                'status': 'completed',
                **results
            })
            
            # Save updated completed list
            with open('data/completed-videos.json', 'w') as f:
                json.dump(completed, f, indent=2)
            
            # Remove from pending
            pending['pendingVideos'].remove(video)
    
    # Save updated pending list
    with open('data/pending-videos.json', 'w') as f:
        json.dump(pending, f, indent=2)

if __name__ == '__main__':
    main()