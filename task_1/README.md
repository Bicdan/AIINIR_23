Первое задание курса "Индустриальные исследования в искусственном интеллекте".

Как собрать: `docker build . --network host -t llm_username:v1`

Как запустить: `docker run -p 8080:8080 llm_username:v1`

Как отправить запрос: `curl -X POST -H "Content-Type: application/json" -d '{"message": "Вопрос пользователя", "user_id": "404"}' http://localhost:8080/message`