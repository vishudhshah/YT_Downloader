# YT_Downloader

A simple Python script for downloading YouTube videos.

## Requirements

- Python 3.11+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp): `pip install -r requirements.txt`
- [ffmpeg](https://ffmpeg.org/) (merges video + audio): `brew install ffmpeg`
- [Node.js](https://nodejs.org/) 22+ (solves YouTube JS challenges), available on your `PATH`
- Google Chrome, logged in to YouTube (cookies are read from it)

## Usage

```sh
python3 main.py
```

Paste a YouTube URL when prompted. The video downloads as MP4 with English subtitles (if available) into the current directory.
