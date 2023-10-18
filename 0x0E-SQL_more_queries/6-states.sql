-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
CREATE DATABASE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255) NOT NULL
	);
