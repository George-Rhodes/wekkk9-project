FROM mysql:5.7
COPY . .
COPY CreateTable.sql /docker-entrypoint-initdb.d/db
ENTRYPOINT ['sudo source','./URI.sh']