# Stack & EmailClient Project

Данный проект состоит из двух независимых частей:

1. **Stack Checker** — реализация стека и проверка сбалансированности скобок.
2. **EmailClient** — класс для отправки и получения писем .

---
```
project/
├── stack_checker.py
├── email_client.py
├── test_stack.py
├── test_is_balanced.py
├── README.md
├── requirements.txt
└── .gitignore
```


## 1. Stack Checker

Файл: `stack_checker.py`

### Функционал
- Класс `Stack` с методами:
  - `is_empty()` — проверка пустоты стека
  - `push(item)` — добавление элемента
  - `pop()` — извлечение элемента с удалением
  - `peek()` — просмотр верхнего элемента без удаления
  - `size()` — количество элементов
- Функция `is_balanced(s)` — проверка, сбалансированы ли скобки в строке.


### Тесты (необязательно)

В корне есть файлы:

`test_stack.py`

`test_is_balanced.py`

Запуск тестов:

Установите зависимости:

```bash

pip install -r requirements.txt 
pytest
 ```

## 2. EmailClient
Файл: `email_client.py`

### Функционал
- Отправка писем 
- Получение последних писем  с фильтрацией по критерию поиска
- Безопасная работа с паролями через переменные окружения

### Запуск

Перед запуском установите переменные окружения:

```bash

export EMAIL_ADDRESS="your_email@example.com"
export EMAIL_PASSWORD="your_password_or_app_password" 
python email_client.py
```


