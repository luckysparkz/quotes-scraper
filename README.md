# Quotes Scraper

Асинхронный парсер `quotes.toscrape.com/js` с сохранением в CSV и браузерной автоматизацией.

## Используемые технологии
- Python 3.14
- Patchright + asyncio
- CSV
- mypy
- logging

## Возможности
- Асинхронный парсинг с использованием браузерной автоматизации для элементов, которые загружаются динамически через JavaScript
- Менее детектируемый парсинг благодаря использованию форка Playwright: Patchright
- Логирование на каждом этапе, в том числе и возможных ошибок
- Хранение данных в CSV

## Почему обычный HTTP-запрос здесь не работает
Сайт `quotes.toscrape.com/js` рендерит цитаты через JavaScript - они отсутствуют в исходном HTML, который возвращает сервер. Обычный HTTP-клиент получает пустую страницу:

```python
import httpx
response = httpx.get("https://quotes.toscrape.com/js")
print(".quote" in response.text)  # False
```

Playwright/Patchright запускает реальный браузер, выполняет JS и только после этого отдаёт итоговый DOM - поэтому для таких сайтов необходима браузерная автоматизация.

## Запуск
```bash
pip install -r requirements.txt
python main.py
```

## Пример результатов парсинга
### Все цитаты с первой страницы
| Text | Author | Tags |
|---|---|---|
| “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.” | Albert Einstein | change, deep-thoughts, thinking, world |
| “It is our choices, Harry, that show what we truly are, far more than our abilities.” | J.K. Rowling | abilities, choices |
| “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.” | Albert Einstein | inspirational, life, live, miracle, miracles |
| “The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.” | Jane Austen | aliteracy, books, classic, humor |
| “Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.” | Marilyn Monroe | be-yourself, inspirational |
| “Try not to become a man of success. Rather become a man of value.” | Albert Einstein | adulthood, success, value |
| “It is better to be hated for what you are than to be loved for what you are not.” | André Gide | life, love |
| “I have not failed. I've just found 10,000 ways that won't work.” | Thomas A. Edison | edison, failure, inspirational, paraphrased |
| “A woman is like a tea bag; you never know how strong it is until it's in hot water.” | Eleanor Roosevelt | misattributed-eleanor-roosevelt |
| “A day without sunshine is like, you know, night.” | Steve Martin | humor, obvious, simile |

## Примечания
- Была добавлена задержка в 0.5с для демонстрации одного из способов избежания блокировки на реальном проекте