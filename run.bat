@echo off
REM Set paths and parameters
set PLAYLIST_URL="https://www.youtube.com/playlist?list=PL64gNG-f59ZbK9JfyiZHlu2r7bEyHf2pR"
set OUTPUT_TEMPLATE="P:\Movies\Motorbike Tales South America\EP%%(playlist_index)02d.%%(ext)s"
set ARCHIVE_FILE="P:\Movies\Motorbike Tales South America\downloaded.txt"
set FFMPEG_PATH="C:\tools\ffmpeg-2025-07-17-git-bc8d06d541-full_build\bin"
set FORMAT_STRING="bestvideo[height<=2160]+bestaudio/best[height<=2160]"

REM Call the Python script
python download_playlist.py ^
  --url %PLAYLIST_URL% ^
  --output %OUTPUT_TEMPLATE% ^
  --archive %ARCHIVE_FILE% ^
  --ffmpeg %FFMPEG_PATH% ^
  --format %FORMAT_STRING%

pause
