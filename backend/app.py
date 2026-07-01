from fastapi import FastAPI
from routes import incidents
from routes import pam
from routes import dam
from routes import risk
from database.database import engine
from database.models import Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="PAM-DAM AI Security API",
    version="2.0.0",
    description="AI Powered PAM & DAM Security Platform"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "project": "PAM-DAM AI Security Platform",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


app.include_router(pam.router)
app.include_router(dam.router)
app.include_router(risk.router)
app.include_router(incidents.router)