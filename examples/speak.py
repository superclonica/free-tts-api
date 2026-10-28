"""Voice a text with the SuperClonica speech API and save the file.

pip install requests
SUPERCLONICA_KEY=sc_... python speak.py "Hello from Python!"
"""
import os
import sys

import requests

API = "https://superclonica.com/api/v1/speech"


def speak(text, voice="F1", language="en", audio_format="mp3"):
    answer = requests.post(
        API,
        headers={"Authorization": "Bearer " + os.environ["SUPERCLONICA_KEY"]},
        json={"text": text, "voice": voice, "language": language, "format": audio_format},
        timeout=120,
    )
    if answer.status_code == 429:
        raise SystemExit(f"Daily free time is used up; try again in {answer.headers.get('retry-after')} s")
    answer.raise_for_status()
    return answer.content


if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) or "Hello! This voice comes from a free API."
    with open("speech.mp3", "wb") as file:
        file.write(speak(text))
    print("saved speech.mp3")
