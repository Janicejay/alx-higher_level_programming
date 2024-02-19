-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create table if it does not exist and populate it
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
