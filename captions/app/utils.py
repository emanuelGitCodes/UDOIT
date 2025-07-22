import os
import requests
import openai
from flask import current_app


def download_video(url: str, dest_dir: str, filename_prefix: str) -> str:
    os.makedirs(dest_dir, exist_ok=True)
    local_path = os.path.join(dest_dir, f"{filename_prefix}.mp4")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    return local_path


def transcribe_video(path: str, language: str) -> str:
    openai.api_key = current_app.config["OPENAI_API_KEY"]
    with open(path, "rb") as f:
        transcript = openai.Audio.transcribe(
            "whisper-1", f, response_format="vtt", language=language
        )
    return transcript
