# NER API

API находит именованные сущности (имена, организации, локации) в тексте.
Модель: `dslim/distilbert-NER` с Hugging Face.

![CI](https://github.com/Razdva7/ner-api/actions/workflows/ci.yml/badge.svg)

## Live Demo (Streamlit)
https://ner-api-v7q3ruoewjxxejadubu2hk.streamlit.app/

## Локальный запуск (FastAPI)
pip install -r requirements.txt
uvicorn main:app --reload

## Streamlit локально
streamlit run streamlit_app.py

## Тесты
pytest -v
