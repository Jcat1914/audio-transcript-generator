import os
import sys
import argparse
import whisper
from datetime import timedelta

def format_timestamp(seconds: float):
    td = timedelta(seconds=seconds)
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def write_srt(segments, srt_path):
    with open(srt_path, 'w', encoding='utf-8') as f:
        for i, segment in enumerate(segments, start=1):
            start = format_timestamp(segment['start'])
            end = format_timestamp(segment['end'])
            text = segment['text'].strip()
            f.write(f"{i}\n{start} --> {end}\n{text}\n\n")

def write_txt(text, txt_path):
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)

def main():
    parser = argparse.ArgumentParser(description="Transcribe audio files using OpenAI Whisper.")
    parser.add_argument("input", help="Path to the local audio file")
    parser.add_argument("--model", default="base", help="Whisper model to use (tiny, base, small, medium, large)")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: File '{args.input}' not found.")
        sys.exit(1)

    print(f"Loading Whisper model '{args.model}'...")
    try:
        model = whisper.load_model(args.model)
    except Exception as e:
        print(f"Error loading model: {e}")
        sys.exit(1)

    print(f"Transcribing '{args.input}'...")
    try:
        # result contains 'text' and 'segments'
        result = model.transcribe(args.input)
    except Exception as e:
        print(f"Error during transcription: {e}")
        print("Note: Ensure 'ffmpeg' is installed on your system.")
        sys.exit(1)

    base_name = os.path.splitext(args.input)[0]
    txt_path = f"{base_name}.txt"
    srt_path = f"{base_name}.srt"

    print(f"Saving transcript to {txt_path}...")
    write_txt(result['text'], txt_path)

    print(f"Saving subtitles to {srt_path}...")
    write_srt(result['segments'], srt_path)

    print("Done!")

if __name__ == "__main__":
    main()
