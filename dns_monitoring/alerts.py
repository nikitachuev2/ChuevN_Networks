import json
import smtplib
from dataclasses import dataclass
from email.message import EmailMessage
from typing import Literal, Optional

import httpx

from config import get_settings

Channel = Literal["slack", "telegram", "email"]


@dataclass
class Alert:
    level: Literal["info", "warning", "critical"]
    title: str
    message: str

    def format_markdown(self) -> str:
        """Небольшое форматирование для Slack / Telegram."""
        emoji = {"info": "ℹ️", "warning": "⚠️", "critical": "🔥"}[self.level]
        return f"*{emoji} {self.title}*\n```{self.message}```"


def send_alert(alert: Alert, channel: Channel, target: Optional[str] = None) -> None:
    """
    Универсальный отправитель.

    Parameters
    ----------
    alert : Alert
        Объект события.
    channel : {"slack","telegram","email"}
        Куда шлём.
    target : str, optional
        ID чата / email / webhook override.
    """
    cfg = get_settings()
    if channel == "slack":
        _send_slack(alert, target or cfg.slack_webhook)
    elif channel == "telegram":
        print("Будет отправлено", alert)  
    elif channel == "email":
        _send_email(alert, target)
    else:
        raise ValueError(f"Неизвестный канал {channel}")


def _send_slack(alert: Alert, webhook: Optional[str]) -> None:
    if not webhook:
        print("Пропущено")
        return
    payload = {"text": alert.format_markdown(), "mrkdwn": True}
    httpx.post(webhook, json=payload, timeout=4.0)
    print("Отправлено предупреждение")


def _send_email(alert: Alert, to_addr: Optional[str]) -> None:
    if not to_addr:
        print("Предупреждение пропущено")
        return
    msg = EmailMessage()
    msg["Subject"] = alert.title
    msg["From"] = f"noreply@{get_settings().base_domain}"
    msg["To"] = to_addr
    msg.set_content(alert.message)

    with smtplib.SMTP("localhost") as smtp:
        smtp.send_message(msg)
    print("Отправлено")


if __name__ == "__main__":
    demo = Alert("critical", "Demo alert", "Поступил вредоносный DNS-запрос из AS12345")
    send_alert(demo, "slack")