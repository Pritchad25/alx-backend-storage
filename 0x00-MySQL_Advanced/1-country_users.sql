-- Creates a table called user on any database
-- addition of the country attribute
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255),
	country ENUM ('US', 'CO', 'TN') NOT NULL
)
