from fastapi import FastAPI
from database import Base, engine

# Создать таблицы для базы данных
Base.metadata.create_all(bind=engine)

# Объект для Fastapi
app = FastAPI()


from business import business_api
from card_manage import card_api
from user_authentication import user_api


# Запуск проекта FastApi
# uvicorn main:app --reload
