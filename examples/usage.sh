#!/bin/sh
# How much of today's free time is left, and which voices your key can use.
curl -sS https://superclonica.com/api/v1/usage -H "Authorization: Bearer $SUPERCLONICA_KEY"; echo
curl -sS https://superclonica.com/api/v1/voices -H "Authorization: Bearer $SUPERCLONICA_KEY" | cut -c1-600
