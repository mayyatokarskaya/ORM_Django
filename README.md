# ORM_Django Catalog Project

Простой веб-каталог на Django с главной страницей и разделом контактов.

## Особенности
- Главная страница с базовым контентом (`/` или `/home/`)
- Страница контактов (`/contacts/`)
- Статические файлы (CSS)
- Готовые шаблоны (`home.html`, `contacts.html`)

## Установка
1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/mayyatokarskaya/DjangoProject.git
   cd DjangoProject
   ```

2. **Создайте виртуальное окружение** (Python 3.8+):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Запустите сервер**:
   ```bash
   python manage.py runserver
   ```
   Откройте [http://127.0.0.1:8000](http://127.0.0.1:8000) в браузере.

## Структура проекта
```
DjangoProject/
├── catalog/               # Приложение
│   ├── templates/         # Шаблоны
│   │   ├── catalog/
│   │   │   ├── home.html
│   │   │   └── contacts.html
│   ├── static/            # CSS/JS
│   ├── views.py           # Контроллеры
│   └── urls.py            # Маршруты приложения
├── DjangoProject/         # Настройки проекта
│   ├── settings.py
│   └── urls.py            # Главные URL
├── .gitignore
└── requirements.txt       # Зависимости
```

## URL-адреса
- **Главная**: `/` или `/home/`
- **Контакты**: `/contacts/`

## Примеры кода
### Контроллер (views.py)
```python
from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')
```

### Маршруты (catalog/urls.py)
```python

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
]
```
