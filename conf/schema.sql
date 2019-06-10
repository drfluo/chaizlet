-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2019-03-21 14:04:12.433

-- tables
-- Table: class
CREATE TABLE class (
    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name varchar(64) NOT NULL,
    language_foreign_id varchar(20) NOT NULL,
    language_origin_id varchar(20) NOT NULL,
    prof_id varchar(20) NOT NULL
);

-- Table: class_list
CREATE TABLE class_list (
    list_id_fk_cl int NOT NULL,
    class_id_fk_cl int NOT NULL
);

-- Table: language
CREATE TABLE language (
    name varchar(19) PRIMARY KEY
);

-- Table: list
CREATE TABLE list (
    list_id INTEGER PRIMARY KEY AUTOINCREMENT,
    list_name varchar(128) NOT NULL
);

-- Table: photo
CREATE TABLE photo (
    ln_letter char(1) NOT NULL,
    picture blob NOT NULL
);

-- Table: role
CREATE TABLE role (
    name varchar(16) PRIMARY KEY

);

-- Table: translation
CREATE TABLE translation (
    translation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    word_foreign varchar(128) NOT NULL
);

-- Table: translation_word
CREATE TABLE translation_word (
    translation_id_fk_tw int NOT NULL,
    word_id_fk_tw int NOT NULL
);

-- Table: user
CREATE TABLE user (
    first_name varchar(64) NOT NULL,
    last_name varchar(64) NOT NULL,
    username varchar(64) PRIMARY KEY,
    email varchar(666) NOT NULL,
    passwd_hash varchar(255) NOT NULL,
    role_id varchar(18) NOT NULL
);

-- Table: user_class
CREATE TABLE user_class (
    username_fk_uc varchar(64) NOT NULL,
    class_id_fk_uc int NOT NULL
);

-- Table: word
CREATE TABLE word (
    word_id INTEGER PRIMARY KEY AUTOINCREMENT,
    word_origin varchar(128) NOT NULL
);

-- Table: word_list
CREATE TABLE word_list (
    word_id_fk_wl int NOT NULL,
    list_id_fk_wl int NOT NULL
);

-- user

INSERT INTO user (username, passwd_hash, first_name, last_name, email, role_id) 
	VALUES ("Pouet", "14b10468a32dbd4d2be8c996930948818cb1ebdb", "Laureline", "Polli", "polli.laureline@destael.educanet2.ch", "Admin");

INSERT INTO user (username, passwd_hash, first_name, last_name, email, role_id) 
	VALUES ("RaptorDelta999", "14b10468a32dbd4d2be8c996930948818cb1ebdb", "Damien", "Rupp", "rupp.damien@destael.educanet2.ch", "Professeur");

INSERT INTO user (username, passwd_hash, first_name, last_name, email, role_id) 
	VALUES ("LAURELINE", "14b10468a32dbd4d2be8c996930948818cb1ebdb", "Laureline", "POLLI", "lpolli2001@gmail.com", "Elève");

INSERT INTO user (username, passwd_hash, first_name, last_name, email, role_id) 
	VALUES ("DAMIEN.R", "14b10468a32dbd4d2be8c996930948818cb1ebdb", "Damien", "RUPP", "drupp2001@gmail.com", "Elève");


-- language

INSERT INTO language (name) 
	VALUES ("francais");

INSERT INTO language (name)
        VALUES ("russe");

INSERT INTO language (name)
       VALUES ("anglais");

INSERT INTO language (name)
	VALUES ("mandarin simplifié");

INSERT INTO language (name)
        VALUES ("Dothraki");


-- class

INSERT INTO class (class_id, class_name, language_foreign_id, language_origin_id, prof_id)
	VALUES (1, "Alpha-Mike", "francais", "russe", "Pouet");

-- class-user

INSERT INTO user_class (username_fk_uc, class_id_fk_uc)
		VALUES 
			("LAURELINE", 2),
			("LAURELINE", 1),
			("DAMIEN.R", 1);

-- class-list

INSERT INTO class_list (list_id_fk_cl, class_id_fk_cl)
		VALUES
			(1, 1),
			(2, 1),
			(3, 2);
-- list

INSERT INTO list (list_id, list_name)
		VALUES 
			(1, "champ lexical de la mer"),
			(2, "champ lexical des animaux"),
			(3, "animaux");
-- word-list

INSERT INTO word_list (word_id_fk_wl, list_id_fk_wl)
		VALUES 
			(1, 1),
			(2, 2),
			(3, 2),
			(4, 3);

-- translation_word

INSERT INTO translation_word (translation_id_fk_tw, word_id_fk_tw)
		VALUES 
			(1, 1),
			(2, 2),
                	(3, 3),
			(4, 4);
-- word

INSERT INTO word (word_id, word_origin)
		VALUES
                	(1, "podvodnaya lodka"),
                	(2, "loshad'"),
                	(3, "morskaya cherepakha"),
			(4, "dog");
-- translation 

INSERT INTO translation (translation_id, word_foreign)
		VALUES 
			(1, "sous-marin"),
         	        (2, "cheval"),
         	        (3, "tortue de mer"),
			(4, "chien")
