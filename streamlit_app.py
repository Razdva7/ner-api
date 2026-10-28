import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="NER API", layout="centered")
st.title("NER API")
st.caption("Модель: dslim/distilbert-NER")

@st.cache_resource
def get_ner():
    return pipeline("ner", model="dslim/distilbert-NER", aggregation_strategy="simple")

text = st.text_area("Введите текст", "Elon Musk founded SpaceX in California.")

if st.button("Извлечь сущности"):
    if text.strip():
        with st.spinner("Извлечение..."):
            entities = get_ner()(text)
        if entities:
            st.json([
                {"word": e["word"], "type": e["entity_group"], "score": round(float(e["score"]), 3)}
                for e in entities
            ])
        else:
            st.info("Сущности не найдены")
    else:
        st.warning("Введите текст")
