# n8n Workflow Automation

**No-code workflow: RSS -> фильтрация -> Telegram**

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
[![n8n](https://img.shields.io/badge/n8n-1.54-FF6D5A?logo=n8n)](https://n8n.io)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Описание

Автоматизация рабочих процессов через n8n:
- Получение RSS-фидов
- Фильтрация и обработка контента
- Отправка в Telegram
- Расписание через APScheduler

---

## Быстрый старт

`ash
git clone https://github.com/Shamanchi/n8n-workflow-automation
cd n8n-workflow-automation
cp .env.example .env
# Настройте .env
docker-compose up -d
`

### Переменные окружения
| Переменная | Описание |
|------------|----------|
| N8N_URL | URL n8n instance |
| N8N_API_KEY | API ключ n8n |
| RSS_FEEDS | Список RSS через запятую |
| TELEGRAM_BOT_TOKEN | Токен бота |
| TELEGRAM_CHAT_ID | ID чата |

---

## Тесты
`ash
pytest -v
`

---

## Docker
`ash
docker build -t n8n-workflow-automation .
docker-compose up -d
`

---

## Структура
`
├── app/
│   ├── api/routes.py
│   ├── core/config.py
│   ├── core/logging.py
│   ├── services/workflow.py
│   └── main.py
├── tests/test_api.py
├── .github/workflows/ci.yml
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
`

---

## CI/CD
GitHub Actions: Ruff, MyPy, Pytest, Docker build

---

## Лицензия
MIT

---

> Источник темы: Каталог портфолио, запись n8n-workflow-automation