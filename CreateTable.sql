CREATE TABLE project;
USE project;
CREATE TABLE IF NOT EXISTS ticks
             (
                          id         INTEGER NOT NULL AUTO_INCREMENT,
                          ticket VARCHAR(6) NOT NULL,
                          prize      VARCHAR(250) NOT NULL,
                          PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `ticks` WRITE;

INSERT INTO `ticks` VALUES (1,'FD15','sorry, you win nothing'),(2,'HH58','sorry, you win nothing'),(3,'AA56','sorry, you win nothing');

UNLOCK TABLES;