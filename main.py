from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from functools import lru_cache

app = FastAPI(title="NER API")

@lru_cache
def get_ner():
    return pipeline("ner", model="dslim/distilbert-NER", aggregation_strategy="simple")

class Item(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/extract")
def extract(item: Item):
    entities = get_ner()(item.text)
    return {
        "text": item.text,
        "entities": [
            {"word": e["word"], "type": e["entity_group"], "score": round(float(e["score"]), 3)}
            for e in entities
        ],
    }
