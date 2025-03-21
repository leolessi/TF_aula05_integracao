FROM postgres:14

COPY init.sql /docker-entrypoint-initdb.d/

ENV POSTGRES_DB=init
ENV POSTGRES_USER=faat
ENV POSTGRES_PASSWORD=faat

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5000