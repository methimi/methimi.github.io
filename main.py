from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests, os

app = FastAPI()

# 🔓 CORS AYARI (EN ÖNEMLİ KISIM)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # istersen sadece github pages domainini yazarsın
    allow_credentials=True,
    allow_methods=["*"],  # OPTIONS dahil
    allow_headers=["*"],
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/visit")
async def visit(req: Request):
    data = await req.json()
    page = data.get("page", "/")

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": f"👀 Yeni ziyaret: {page}"
        }
    )

    return {"ok": True}
