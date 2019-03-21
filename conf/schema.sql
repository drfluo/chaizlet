CREATE TABLE user
(
	username VARCHAR(64) NOT NULL,
	passwd_hash VARCHAR(64) NOT NULL,
	first_name VARCHAR(64) DEFAULT NULL,
	last_name VARCHAR(64) DEFAULT NULL,
	email VARCHAR(128) DEFAULT NULL
); 

INSERT INTO user (username, passwd_hash, first_name, last_name, email) 
	VALUES ("Pouet", "14b10468a32dbd4d2be8c996930948818cb1ebdb", "Laureline", "Polli", "polli.laureline@destael.educanet2.ch");

INSERT INTO user (username, passwd_hash, first_name, last_name, email) 
	VALUES ("RaptorDelta999", "14b10468a32dbd4d2be8c996930948818cb1ebdb", "Damien", "Rupp", "rupp.damien@destael.educanet2.ch");

