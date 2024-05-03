FROM mysql

EXPOSE 3306

COPY ./Infra/Scripts.sql /docker-entrypoint-initdb.d/

ENV MYSQL_ROOT_PASSWORD=monkey
ENV MYSQL_DATABASE=monkey_consulting
ENV MYSQL_USER=monkey
ENV MYSQL_PASSWORD=monkey

