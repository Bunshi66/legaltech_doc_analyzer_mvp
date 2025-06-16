# Используем официальный образ Python как базовый
FROM python:3.10-slim-buster

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл requirements.txt в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все остальные файлы приложения в рабочую директорию
COPY . .

# Открываем порт 5000 для входящих подключений
EXPOSE 5000

# Определяем команду, которая будет выполняться при запуске контейнера
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]