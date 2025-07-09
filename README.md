# Sentiment Analysis API (Flask + SQLite)

Микросервис для анализа тональности текстовых отзывов с возможностью фильтрации и хранения результатов.

## 🚀 Особенности

- Определение тональности (positive/neutral/negative) русскоязычного текста
- Хранение отзывов в SQLite базе данных
- RESTful API с документацией
- Фильтрация отзывов по тональности("настроению")
- Контейнеризация с Docker
- Расширяемый словарь тональности

## 🛠️ Технологии
- Python 3.9+
- Docker
- SQLite


#### API Endpoints
| Метод | Эндпоинт              | Параметры        | Описание                           |
|-------|-----------------------|------------------|------------------------------------|
| GET   | `/api/reviews/get`    | `sentiment`      | Фильтрация отзывов по "настроению" |
| POST  | `/api/reviews/create` | `text` в json формате | Создание и анализ отзыва           |

### 📡 Примеры запросов API
1. Создание отзыва

Endpoint: POST /api/reviews

Запрос:

```bash
curl -X POST http://localhost:5000/api/reviews \
-H "Content-Type: application/json" \
-d '{"text":"Потрясающий сервис! Быстро и удобно."}'
```

Успешный ответ (201 Created):

```
{
  "id": 1,
  "text": "Потрясающий сервис! Быстро и удобно.",
  "sentiment": "positive",
  "created_at": "2023-05-20T15:30:45.123456Z"
}
```

Ошибка (400 Bad Request):
```
json
{
  "error": "Text is required",
  "status": 400
}
```

2. Вывод отзывов по фильтру
Endpoint: GET /api/reviews

Варианты запросов:

Без фильтров:
```bash
curl http://localhost:5000/api/reviews
```
С фильтром по тональности:
```bash
curl "http://localhost:5000/api/reviews?sentiment=negative"
```
Успешный ответ (200 OK):
```
[
  {
    "id": 1,
    "text": "Потрясающий сервис!..",
    "sentiment": "positive",
    "created_at": "2023-05-20T15:30:45.123456Z"
  },
  {
    "id": 2,
    "text": "Работает ужасно медленно...",
    "sentiment": "negative",
    "created_at": "2023-05-20T15:35:22.654321Z"
  }
]
```

## 🚀 Как запустить проект

```bash
docker-compose up --build