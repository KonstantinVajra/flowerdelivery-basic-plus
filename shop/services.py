import os

import requests


def send_telegram_notification(text: str, parse_mode: str | None = None) -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text,
    }

    if parse_mode:
        payload["parse_mode"] = parse_mode

    resp = requests.post(url, data=payload, timeout=10)

    try:
        resp.raise_for_status()
    except requests.HTTPError as exc:
        raise RuntimeError(
            f"Telegram error: {resp.status_code} {resp.text}"
        ) from exc


def send_telegram_photo(photo_url: str, caption: str, parse_mode: str | None = None) -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        return

    url = f"https://api.telegram.org/bot{token}/sendPhoto"

    payload = {
        "chat_id": chat_id,
        "photo": photo_url,
        "caption": caption,
    }
    if parse_mode:
        payload["parse_mode"] = parse_mode

    resp = requests.post(url, data=payload, timeout=10)
    try:
        resp.raise_for_status()
    except requests.HTTPError as exc:
        raise RuntimeError(
            f"Telegram error: {resp.status_code} {resp.text}"
        ) from exc