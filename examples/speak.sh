#!/bin/sh
# Voice a line and save it as MP3. Get a free key at https://superclonica.com/en/speech-api
curl -sS https://superclonica.com/api/v1/speech \
  -H "Authorization: Bearer $SUPERCLONICA_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello! This voice comes from a free API.", "voice": "F1", "language": "en", "format": "mp3"}' \
  --fail-with-body -o hello.mp3 && echo "saved hello.mp3"
