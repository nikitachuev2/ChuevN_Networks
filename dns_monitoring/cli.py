import click

from analytics import top_asns, daily_growth
from alerts import Alert, send_alert


@click.group()
def cli() -> None:  # noqa: D401
    """Утилиты rs-dnswatch (неподключённые)."""
    pass


@cli.command("top")
@click.option("--limit", "-n", default=10, help="Сколько ASN выводить.")
def cmd_top(limit: int) -> None:
    """Показать самые активные ASN."""
    print(top_asns(limit).to_string(index=False))


@cli.command("growth")
def cmd_growth() -> None:
    """Суточный прирост логов."""
    print(daily_growth().tail().to_string())


@cli.command("demo-alert")
@click.option("--channel", default="slack", type=click.Choice(["slack", "telegram", "email"]))
def cmd_demo_alert(channel: str) -> None:
    """Отправить тестовый alert."""
    alert = Alert("info", "Demo-alert", "🚀 CLI-alert отправлен успешно")
    send_alert(alert, channel)


if __name__ == "__main__":
    cli()
