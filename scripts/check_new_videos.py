import os
import json
from googleapiclient.discovery import build

def main():
    youtube = build('youtube', 'v3', developerKey=os.environ['YOUTUBE_API_KEY'])
    
    # Get latest videos from channel
    request = youtube.search().list(
        part='snippet',
        channelId='UCxb8c4X11Q6m3PsUhA2oheg',  # Greg's channel ID
        order='date',
        type='video'
    )
    response = request.execute()
    
    # Update database files
    # Implementation details here

if __name__ == '__main__':
    main()