from fastapi import FastAPI


from libvoikko import Voikko


app = FastAPI()

v = Voikko('fi')

@app.get("/analyze")
async def analyze(word: str):
    return v.analyze(word)

@app.get("/spell")
async def spell(word: str):
    return { "spelling" : v.spell(word) }

@app.get("/suggest")
async def suggest(word: str):
    return v.suggest(word)

@app.get("/hyphenate")
async def hyphenate(word: str):
    return { "hyphenated" : v.hyphenate(word), "pattern": v.getHyphenationPattern(word) }
