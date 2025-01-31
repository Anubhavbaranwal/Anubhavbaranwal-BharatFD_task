from fastapi import FastAPI, Query
from .models import FAQ, Base
from .database import engine, SessionLocal
from .routers import faq


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(faq.router)