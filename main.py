import yt_dlp

url = ''
while not url:
    url = input('YouTube URL: ').strip()
path = '.'

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': f'{path}/%(title)s.%(ext)s',
    'merge_output_format': 'mp4',
    'cookiesfrombrowser': ('chrome',),
    'js_runtimes': {'node': {'path': '/opt/homebrew/bin/node'}},
    'remote_components': ['ejs:github'],
    'writesubtitles': True,
    'writeautomaticsub': True,
    'subtitleslangs': ['en'],
    'quiet': True,
    'no_warnings': True,
    'noprogress': False,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    print(f'Downloading: {info["title"]}')
    ydl.process_ie_result(info, download=True)
    print(f'Downloaded to {path}/')
