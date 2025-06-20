# Legal Document Analyzer MVP

## Описание проекта
Данный проект представляет собой минимально жизнеспособный продукт (MVP) для анализа юридических документов (исков, договоров, актов) с целью извлечения ключевых сущностей (на основе BERT-подобных моделей), последующей rule-based валидации и предоставления структурированных результатов.

## Архитектура
Проект разработан с использованием микросервисной архитектуры, включающей:
- **Frontend:** Интерфейс пользователя (Next.js).
- **API Gateway:** Основная точка входа для всех запросов к бэкенду (Flask).
- **Document Service:** Микросервис для управления хранением документов и их метаданных.
- **ML Analyzer Service (планируется):** Микросервис для выполнения анализа документов с использованием BERT-подобных моделей.
- **MongoDB:** База данных для хранения метаданных документов и результатов анализа.
- **Apache Kafka:** Распределенная очередь сообщений для асинхронного взаимодействия между микросервисами.

## Стек технологий
- **Backend:** Python, Flask
- **Frontend:** React, Next.js, TypeScript, Tailwind CSS
- **База данных:** MongoDB
- **Очередь сообщений:** Apache Kafka
- **Контейнеризация:** Docker, Docker Compose
- **ML:** BERT-подобные модели (для анализа текста)

## Запуск проекта (локально)

1.  **Клонирование репозитория:**
    ```bash
    git clone [https://github.com/Bunshi66/legaltech_doc_analyzer_mvp.git](https://github.com/Bunshi66/legaltech_doc_analyzer_mvp.git)
    cd legaltech_doc_analyzer_mvp
    ```

2.  **Запуск инфраструктурных сервисов (MongoDB, Kafka, Zookeeper) с помощью Docker Compose:**
    ```bash
    docker-compose up -d mongodb zookeeper kafka
    ```
    * После запуска убедитесь, что контейнеры работают: `docker ps`

3.  **Запуск бэкенд-сервисов:**
    * Инструкции по запуску `api-gateway` и `document-service` будут добавлены позже.

4.  **Запуск фронтенд-приложения:**
    * Инструкции по запуску `frontend` будут добавлены позже.

## Командная разработка (Упрощенный GitHub Flow)
Мы используем упрощенный GitHub Flow:
- **`main` ветка:** Всегда стабильная, готовая к деплою.
- **`feature/название-фичи` ветки:** Для каждой новой задачи (фичи или исправления).
- **Pull Requests (PRs):** Все изменения вливаются в `main` через PR после код-ревью.

## Контакты
- Вячеслав (Project Manager, Backend Lead, Solutions Architect, ML Engineer, DevOps)
- Елисей (Frontend Developer)
- Максим (Backend Developer)
- Георгий (Creative inspiration and just a good guy)