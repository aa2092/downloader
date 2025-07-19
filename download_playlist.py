import yt_dlp
import argparse
import os

def download_playlist(url, output_template, archive_file, ffmpeg_path=None, format_selector=None):
    os.makedirs(os.path.dirname(output_template), exist_ok=True)

    ydl_opts = {
        'outtmpl': output_template,
        'format': format_selector or 'best',
        'ignoreerrors': True,
        'download_archive': archive_file,
        'nooverwrites': True,
    }

    if ffmpeg_path:
        ydl_opts['ffmpeg_location'] = ffmpeg_path

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download a YouTube Playlist with yt-dlp.')
    parser.add_argument('--url', required=True, help='YouTube playlist URL')
    parser.add_argument('--output', required=True, help='Output file template, e.g., P:\\path\\to\\folder\\EP%%(playlist_index)02d.%%(ext)s')
    parser.add_argument('--archive', required=True, help='Path to download archive file')
    parser.add_argument('--ffmpeg', default=None, help='Path to ffmpeg binary directory (optional)')
    parser.add_argument('--format', default='best', help='yt-dlp format selector (default: best)')

    args = parser.parse_args()

    download_playlist(
        url=args.url,
        output_template=args.output,
        archive_file=args.archive,
        ffmpeg_path=args.ffmpeg,
        format_selector=args.format
    )
