import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="NER API", layout="centered")
st.title("NER API")
st.caption("Модель: dslim/distilbert-NER")

@st.cache_resource
def get_ner():
    return pipeline(
        "ner",
        model="dslim/distilbert-NER",
        aggregation_strategy="first",
    )

text = st.text_area("Введите текст", "Elon Musk founded SpaceX in California.")

if st.button("Извлечь сущности"):
    if text.strip():
        with st.spinner("Извлечение..."):
            entities = get_ner()(text)

        merged = []
        for e in entities:
            w = e["word"]
            if w.startswith("##") and merged and merged[-1]["type"] == e["entity_group"]:
                merged[-1]["word"] += w[2:]
                merged[-1]["score"] = round(min(merged[-1]["score"], float(e["score"])), 3)
            else:
                merged.append({
                    "word": w.replace("##", ""),
                    "type": e["entity_group"],
                    "score": round(float(e["score"]), 3),
                })

        if merged:
            st.json(merged)
        else:
            st.info("Сущности не найдены")
    else:
        st.warning("Введите текст")
