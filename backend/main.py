from fastapi import FastAPI
from auth import router as auth_router
from form941 import router as form941_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(form941_router, prefix="/form941")