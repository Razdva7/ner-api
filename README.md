# NER API

API находит именованные сущности в тексте.
Модель: `dslim/distilbert-NER` с Hugging Face.

## Запуск
pip install -r requirements.txt
uvicorn main:app --reload

## Тесты
pytest -v
