-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2019-03-21 14:04:12.433

-- tables
-- Table: class
CREATE TABLE class (
    id INTEGER PRIMARY KEY,
    class_name varchar(64) NOT NULL,
    language_foreign_id int NOT NULL,
    language_origin_id int NOT NULL
);

-- Table: class_list
CREATE TABLE class_list (
    list_id int NOT NULL,
    class_id int NOT NULL
);

-- Table: language
CREATE TABLE lang (
    id INTEGER PRIMARY KEY,
    name varchar(19) NOT NULL,
);

-- Table: list
CREATE TABLE list (
    id INTEGER PRIMARY KEY,
    list_name varchar(128) NOT NULL,
);

-- Table: photo
CREATE TABLE photo (
    ln_letter char(1) NOT NULL,
    picture blob NOT NULL,
);

-- Table: role
CREATE TABLE role (
    id INTEGER PRIMARY KEY,
    name varchar(16) NOT NULL,
);

-- Table: translation
CREATE TABLE translation (
    id INTEGER PRIMARY KEY,
    word varchar(128) NOT NULL,
);

-- Table: translation_word
CREATE TABLE translation_word (
    translation_id int NOT NULL,
    word_id int NOT NULL
);

-- Table: user
CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    first_name varchar(64) NOT NULL,
    last_name varchar(64) NOT NULL,
    username varchar(64) NOT NULL,
    email varchar(666) NOT NULL,
    passwd_hash varchar(255) NOT NULL,
    role_id int NOT NULL
);

-- Table: user_class
CREATE TABLE user_class (
    user_id int NOT NULL,
    class_id int NOT NULL
);

-- Table: word
CREATE TABLE word (
    id int NOT NULL,
    word_origin varchar(128) NOT NULL,
);

-- Table: word_list
CREATE TABLE word_list (
    word_id int NOT NULL,
    list_id int NOT NULL
);

INSERT INTO user (username, passwd_hash, first_name, last_name, email, role_id) 
	VALUES ("Pouet", "14b10468a32dbd4d2be8c996930948818cb1ebdb", "Laureline", "Polli", "polli.laureline@destael.educanet2.ch", 1);

INSERT INTO user (username, passwd_hash, first_name, last_name, email, role_id) 
	VALUES ("RaptorDelta999", "14b10468a32dbd4d2be8c996930948818cb1ebdb", "Damien", "Rupp", "rupp.damien@destael.educanet2.ch", 1);

INSERT INTO user (username, passwd_hash, first_name, last_name, email, role_id) 
	VALUES ("LAURELINE", "14b10468a32dbd4d2be8c996930948818cb1ebdb", "Laureline", "POLLI", "lpolli2001@gmail.com", 2);

INSERT INTO user (username, passwd_hash, first_name, last_name, email, role_id) 
	VALUES ("DAMIEN.R", "14b10468a32dbd4d2be8c996930948818cb1ebdb", "Damien", "RUPP", "drupp2001@gmail.com", 2);


-- language

INSERT INTO lang (name) 
	VALUES ("francais");
INSERT INTO lang (name)    
        VALUES ("allemand");
INSERT INTO lang (name)    
        VALUES ("anglais");



