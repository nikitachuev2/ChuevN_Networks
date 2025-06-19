# Система мониторинга использования DNS-резолверов (dns monitoring)

## Требования к проекту

- Docker
- docker-compose
- Домен для Let's Encrypt или `localhost.local`

## Запуск системы мониторинга
Переход к папке dnsmon:
```bash
bash certbot.sh
docker-compose up --build
переход по адресу: http://localhost:8000/
** Wildcard‑сертификат и SSL отсутсвуют в сборке