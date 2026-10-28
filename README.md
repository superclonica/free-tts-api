# Free Text to Speech API

A free text-to-speech REST API: **3 minutes of audio a day, no card, no trial that ends.**
One `POST` returns the audio file. 31 languages, ten stock voices and every voice of the
[SuperClonica catalog](https://superclonica.com/en/explore) — narrators, announcers, characters — on any plan, the free one included.

```sh
curl https://superclonica.com/api/v1/speech \
  -H "Authorization: Bearer $SUPERCLONICA_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello! This voice comes from a free API.", "voice": "F1", "language": "en", "format": "mp3"}' \
  -o hello.mp3
```

## Get a free key

1. Open [superclonica.com/en/speech-api](https://superclonica.com/en/speech-api).
2. Sign in with Google or GitHub.
3. Create a key. It starts with `sc_` and is shown once: store it as `SUPERCLONICA_KEY`.

## What you get

| | Free | Paid plans |
|---|---|---|
| Audio | 3 minutes a day | from 3 minutes per 10-minute window ($5/month) up to 65 minutes per window ($50/month) |
| Voices | stock + whole catalog + your own trained voices | the same |
| Languages | 31 | 31 |
| Card | not needed | paid from the site wallet |

Prices and limits as of October 2026; the [speech API page](https://superclonica.com/en/speech-api) has the current ones.

## API

`POST https://superclonica.com/api/v1/speech` with `Authorization: Bearer sc_...` and a JSON body:

| Field | | |
|---|---|---|
| `text` | required | up to 20,000 characters |
| `voice` | required | `M1`–`M5`, `F1`–`F5`, or the ID of a catalog voice (shown on its page) |
| `language` | required | a language code such as `en`, `es`, `de`, `fr`, `ru`, `ja`, `ko` |
| `format` | optional | `ogg` (default, smallest), `mp3` or `wav` |
| `stream` | optional | `true` sends the audio as it is made, so playback can start before the whole text is voiced |

The answer is the audio file. Unknown fields are refused with `422`, so a setting that is not
supported never fails silently. When the daily free time is used up, the answer is `429` with a
`Retry-After` header. A text longer than the whole allowance is refused with `413`.

`GET /api/v1/usage` shows the seconds used and left; `GET /api/v1/voices` lists the voices your key can use.

## Examples

- [`examples/speak.sh`](examples/speak.sh) — curl
- [`examples/speak.py`](examples/speak.py) — Python with `requests`
- [`examples/speak.mjs`](examples/speak.mjs) — Node.js 18+, no packages
- [`examples/usage.sh`](examples/usage.sh) — remaining time and available voices

## Languages

English, Spanish, Portuguese, French, German, Italian, Dutch, Swedish, Danish, Finnish, Estonian,
Latvian, Lithuanian, Polish, Czech, Slovak, Slovenian, Croatian, Hungarian, Romanian, Bulgarian,
Greek, Ukrainian, Russian, Turkish, Arabic, Hindi, Vietnamese, Indonesian, Japanese and Korean.
Chinese is not supported yet.

## Rather run it offline?

The same voices run on your own computer, free and without limits, with the open-source engine:

```sh
pip install superclonica-cpu
superclonica --text "Hello!" --voice F1 --lang en --output hello.wav
```

See [superclonica-cpu on PyPI](https://pypi.org/project/superclonica-cpu/).

## Voices and rights

The stock voices `M1`–`M5` and `F1`–`F5` may be used commercially under the OpenRAIL-M license of
the [Supertonic 3](https://huggingface.co/supertone-oss-archive/supertonic-3) model. Character
voices in the catalog are fan-made, for fan and parody use only. Do not use any voice to impersonate a real person.

## License

The examples in this repository are MIT-licensed. The API itself is a service of
[SuperClonica](https://superclonica.com) and follows its terms.
