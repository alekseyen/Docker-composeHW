# Как запустить

Запускаем сервисы:
```bash
docker-compose up --build && docker-compose rm -fsv
```
СХЕМА таблицы `cats`: 
todo

Делаем `GET` запрос в наш сервер(которые идёт в БД):
```bash
 curl -X GET "http://localhost:5000/"
 ```

# Комментарии

1) Для того чтобы контейнеры удалились после того как отработали запускаем: 

`&& docker-compose rm -fsv`

или достаточно запустить

`docker-compose down -v`