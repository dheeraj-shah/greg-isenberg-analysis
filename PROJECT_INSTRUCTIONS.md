# Greg Isenberg Content Analysis Project

## Objective
Automate the collection, transcription, and analysis of Greg Isenberg's YouTube content.

## Process Flow
1. Video Discovery
   - Scrape YouTube channel (@GregIsenberg)
   - Update pending-videos.json with new entries

2. Automated Processing
   - GitHub Actions runs every 6 hours
   - Transcribes pending videos
   - Generates analysis based on project structure
   - Moves processed videos to completed list

3. Content Organization
   - /transcripts/{YYYY}/{video-title}.md
   - /analysis/{YYYY}/{video-title}-analysis.md
   - /trends/monthly-{YYYY-MM}.md

4. Success Criteria
   - No manual intervention required
   - Maintains two lists: pending and completed
   - Auto-updates video database

## Required Files
All templates and structures defined in greg-isenberg-project-knowledge-v2.json