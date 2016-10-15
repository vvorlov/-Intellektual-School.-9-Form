## Настройки

### Использовать русские символы в коде:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
```

### Устанавливаем  Flask:
```python
pip install Flask
```

### Подключаем пакет Flask:
```python
from flask import Flask
```

## Запуск сервера
```python
#создаем переменную с Flask
app = Flask(__name__)

...

#запускаемся, если нас запускают
if __name__ == "__main__":
    app.run()
```


## Обрабатываем запросы
### GET:

```python
@app.route("/hello") #указываем путь
def hello():
    return "Hello, World!"
```

### POST:

```python
@app.route("/postHello", methods=['POST']) #указываем метод
def hello_post():
    return "Hello, World from POST!"
```

Можно использовать сразу несколько методов:

 ```python
 methods=[`GET`, 'POST`]
 ```