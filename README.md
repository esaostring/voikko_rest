# Voikko REST API

Simple FastAPI experiment for [Voikko](https://voikko.puimula.org/).


## Build and start service:

```
docker compose build
docker compose up
```

## Usage examples

### Analyze
```json
$ curl --get --data-urlencode "word=öljyistä" 'http://localhost:8899/analyze' | jq .

[
  {
    "BASEFORM": "öljy",
    "CLASS": "nimisana",
    "FSTOUTPUT": "[Ln][Xp]öljy[X]öljy[Sela][Nm]istä",
    "NUMBER": "plural",
    "SIJAMUOTO": "sisaeronto",
    "STRUCTURE": "=pppppppp",
    "WORDBASES": "+öljy(öljy)"
  },
  {
    "BASEFORM": "öljyinen",
    "CLASS": "laatusana",
    "COMPARISON": "positive",
    "FSTOUTPUT": "[Ln][Xp]öljy[X]öljy[Ll][Xj]inen[X]i[Sp][Ny]stä",
    "NUMBER": "singular",
    "SIJAMUOTO": "osanto",
    "STRUCTURE": "=pppppppp",
    "WORDBASES": "+öljy(öljy)+inen(+inen)"
  }
]
```

### Hyphenate
```json
$ curl --get --data-urlencode "word=öljyistä" 'http://localhost:8899/hyphenate' | jq .
{
  "hyphenated": "öl-jyis-tä",
  "pattern": "  -   - "
}
```

### Check spelling

```json
$ curl --get --data-urlencode "word=tieverkkko" 'http://localhost:8899/spell' | jq .
{
  "spelling": false
}
```
```json
$ curl --get --data-urlencode "word=tieverkko" 'http://localhost:8899/spell' | jq .
{
  "spelling": true
}
```

### Suggest words
```json
$ curl --get --data-urlencode "word=tieverko" 'http://localhost:8899/suggest' | jq .
[
  "tievero",
  "tieverkko",
  "tieverkot",
  "tieveroko",
  "tieverka"
]
```
