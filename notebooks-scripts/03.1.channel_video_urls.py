"""
This script uses yt-dlp to extract all video URLs from a given YouTube channel
without relying on the Google YouTube Data API or API keys.

Workflow:
1. Point to the channel's /videos page using its channel ID.
2. Use yt-dlp with `extract_flat=True` to list entries without downloading media
   or fetching heavy metadata.
3. Filter out non-video entries by validating standard YouTube video IDs
   (exactly 11 characters long).
4. Construct full video URLs for each valid ID.
5. Save the resulting list of URLs to `video_urls.txt` for downstream processing.

Use case:
- Prepare input URLs for further processing pipelines such as transcript
  extraction or metadata collection (e.g., via `get_video_data(url)`),
  with no API keys, no quotas, and automatic pagination handled by yt-dlp.
"""

from yt_dlp import YoutubeDL

CHANNEL_URL = "https://www.youtube.com/channel/UCw5XBZl7_L8t4lQTB246Oug/videos"

ydl_opts = {
    "quiet": True,
    "skip_download": True,
    "extract_flat": True,
}

video_urls = []

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(CHANNEL_URL, download=False)

    for entry in info.get("entries", []):
        vid = entry.get("id")

        # filter only valid video IDs (not channel IDs / playlists)
        if vid and len(vid) == 11:
            video_urls.append(f"https://www.youtube.com/watch?v={vid}")

print(video_urls)

# Save results
with open("video_urls.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(video_urls))
