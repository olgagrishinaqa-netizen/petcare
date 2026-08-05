# PetCare 🐾

PetCare — веб-приложение для ведения информации о домашних питомцах.

## Возможности

- Профиль питомца
- Календарь событий
- Вакцинация
- Обработка от глистов
- Обработка от блох и клещей
- Дневник питомца
- Контроль веса
- Напоминания

## Технологии

- Backend: FastAPI
- Database: PostgreSQL
- Frontend: React
- Docker
- Nginx
- Yandex Cloud

---

# Запуск проекта

## Собрать и запустить

```bash
docker compose up --build
```

## Запустить в фоне

```bash
docker compose up -d
```

## Остановить проект

```bash
docker compose down
```

---

# API

## Проверка работы сервиса

Запрос:

```
GET /health
```

Ответ:

```json
{
  "status": "ok",
  "service": "PetCare API"
}
```

---

# Документация API

После запуска приложения открыть:

```
http://localhost:8000/docs
```
