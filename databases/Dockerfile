FROM postgres:latest

# для заполнения даткой сразу при старте БД
#COPY *.sql /docker-entrypoint-initdb.d/
#ADD create_tables.sql /docker-entrypoint-initdb.d
#RUN chmod a+r /docker-entrypoint-initdb.d/*

ENV POSTGRES_USER admin
ENV POSTGRES_PASSWORD admin
ENV POSTGRES_HOST localhost
ENV POSTGRES_PORT 5432
ENV POSTGRES_DB example
