# Как запустить
В папку `data` необходимо положить ваш .csv файл, который загрузиться в БД(для этого поднимется отдельный сервис).

> ! delimiter у csv должен быть ';' !

Запускаем сервисы:
```bash
docker-compose up --build && docker-compose rm -fsv
```


Делаем `GET` запрос в наш сервер(которые идёт в БД):
```bash
 curl -X GET "http://localhost:5000/"
 ```



# Комментарии

1) Для того чтобы контейнеры удалились после того как отработали запускаем: 

`&& docker-compose rm -fsv`

или достаточно запустить

`docker-compose down -v`

репа: https://gitlab2.atp-fivt.org/tpos2021/podkidysheval-hwdocker