CREATE TABLE IF NOT EXISTS ticks
             (
                          id         INTEGER NOT NULL AUTO_INCREMENT,
                          ticket_num VARCHAR(6) NOT NULL,
                          prize_info      VARCHAR(250) NOT NULL,
                          PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
