import os

import requests


def send_telegram_notification(text: str) -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}

    resp = requests.post(url, data=payload, timeout=10)
    try:
        resp.raise_for_status()
    except requests.HTTPError as exc:
        raise RuntimeError(f"Telegram error: {resp.status_code} {resp.text}") from exc