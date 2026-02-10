from fastapi import FastAPI, Request
import requests, os, datetime

app = FastAPI()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(msg: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": "HTML"
    })

@app.post("/visit")
async def visit(req: Request):
    data = await req.json()

    page = data.get("page")
    ref = data.get("referrer", "Direct")
    ua = data.get("userAgent", "Unknown")
    ip = req.headers.get("x-forwarded-for", "Unknown")
    now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

    msg = f"""
👀 <b>Yeni Ziyaretçi</b>

📄 Sayfa: <code>{page}</code>
🌍 Referrer: {ref}
💻 UA: {ua[:40]}...
📡 IP: {ip}
⏰ {now}
"""

    send_telegram(msg)
    return {"status": "ok"}
