FROM postgres:14

COPY init.sql /docker-entrypoint-initdb.d/

ENV POSTGRES_DB=escola
ENV POSTGRES_USER=faat
ENV POSTGRES_PASSWORD=faat

COPY escola.sql /docker-entrypoint-initdb.d/

EXPOSE 5000