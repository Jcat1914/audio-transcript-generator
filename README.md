# Audio Transcription Tool

A minimal Python script that transcribes local audio files using OpenAI's Whisper model and generates both `.txt` and `.srt` files.

## Prerequisites

1. **Python 3.8+**
2. **ffmpeg**: Required by Whisper for audio processing.
   - macOS: `brew install ffmpeg`
   - Ubuntu/Debian: `sudo apt update && sudo apt install ffmpeg`
   - Windows: Install via [Chocolatey](https://chocolatey.org/) (`choco install ffmpeg`) or download from [ffmpeg.org](https://ffmpeg.org/download.html).

## Setup

1. Clone or download this repository.
2. (Recommended) Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script by providing the path to an audio file (MP3, WAV, M4A, etc.):

```bash
python transcribe.py path/to/your/audio.mp3
```

### Options

- **Model Selection**: You can choose different Whisper models (tiny, base, small, medium, large). The default is `base`.
  ```bash
  python transcribe.py path/to/your/audio.mp3 --model medium
  ```

### Output

The script will generate two files in the same directory as the input audio:
1. `audio.txt`: The full raw transcript.
2. `audio.srt`: Subtitles with timestamps.
