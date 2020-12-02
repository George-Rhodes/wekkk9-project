FROM mysql:5.7
COPY . .
COPY CreateTable.sql /docker-entrypoint-initdb.d/
ENTRYPOINT ['sudo source','./URI.sh']