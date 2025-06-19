from functools import lru_cache
from pathlib import Path
from typing import List, Optional

from pydantic import BaseSettings, Field, validator
from dotenv import load_dotenv

# Подгружаем локальный .env, если существует
load_dotenv(Path(__file__).resolve().parent / ".env")


class Settings(BaseSettings):
    project_name: str = Field("rs-dnswatch", env="PROJECT_NAME")
    db_path: Path = Field("rsdnswatch.db", env="DB_PATH")
    base_domain: str = Field("rs-dnswatch.ru", env="BASE_DOMAIN")

    redis_url: Optional[str] = Field(None, env="REDIS_URL")           # зарезервировано
    slack_webhook: Optional[str] = Field(None, env="SLACK_WEBHOOK")   # для alerts.py

    @validator("base_domain")
    def _strip_https(cls, v: str) -> str:  # noqa: N805
        """Убираем возможный https:// из переменной."""
        return v.replace("https://", "").strip("/")

    @validator("db_path")
    def _ensure_sqlite(cls, v: Path) -> Path:  # noqa: N805
        """Гарантируем расширение .db"""
        return v.with_suffix(".db")

    class Config:
        case_sensitive = False
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    """Кэшированная фабрика: Settings создаётся один раз за процесс."""
    return Settings()


if __name__ == "__main__":
    # Тест-запуск: python config.py
    print("⚙️  Настройки проекта:")
    for field, value in get_settings():
        print(f"{field:12}: {value}")
