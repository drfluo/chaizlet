-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2019-03-21 14:04:12.433

-- tables
-- Table: class
CREATE TABLE class (
    -- id int NOT NULL,
    class_name varchar(64) NOT NULL,
    language_foreign_id int NOT NULL,
    language_origin_id int NOT NULL,
    CONSTRAINT class_pk PRIMARY KEY (id)
);

-- Table: class_list
CREATE TABLE class_list (
    list_id int NOT NULL,
    class_id int NOT NULL
);

-- Table: language_foreign
CREATE TABLE language_foreign (
    -- id int NOT NULL,
    name varchar(19) NOT NULL,
    CONSTRAINT language_foreign_pk PRIMARY KEY (id)
);

-- Table: language_origin
CREATE TABLE language_origin (
    -- id int NOT NULL,
    name varchar(19) NOT NULL,
    CONSTRAINT language_origin_pk PRIMARY KEY (id)
);

-- Table: list
CREATE TABLE list (
    -- id int NOT NULL,
    list_name varchar(128) NOT NULL,
    CONSTRAINT list_pk PRIMARY KEY (id)
);

-- Table: photo
CREATE TABLE photo (
    ln_letter char(1) NOT NULL,
    picture blob NOT NULL,
    CONSTRAINT photo_pk PRIMARY KEY (ln_letter)
);

-- Table: role
CREATE TABLE role (
    -- id int NOT NULL,
    name varchar(16) NOT NULL,
    CONSTRAINT role_pk PRIMARY KEY (id)
);

-- Table: translation
CREATE TABLE translation (
    -- id int NOT NULL,
    word varchar(128) NOT NULL,
    CONSTRAINT translation_pk PRIMARY KEY (id)
);

-- Table: translation_word
CREATE TABLE translation_word (
    translation_id int NOT NULL,
    word_id int NOT NULL
);

-- Table: user
CREATE TABLE user (
    -- id int NOT NULL,
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
    -- id int NOT NULL,
    word_origin varchar(128) NOT NULL,
    CONSTRAINT word_pk PRIMARY KEY (id)
);

-- Table: word_list
CREATE TABLE word_list (
    word_id int NOT NULL,
    list_id int NOT NULL
);

-- foreign keys
-- Reference: class_language_foreign (table: class)
--ALTER TABLE class ADD CONSTRAINT class_language_foreign FOREIGN KEY class_language_foreign (language_foreign_id)
--    REFERENCES language_foreign (id);
--
---- Reference: class_language_origin (table: class)
--ALTER TABLE class ADD CONSTRAINT class_language_origin FOREIGN KEY class_language_origin (language_origin_id)
--    REFERENCES language_origin (id);
--
---- Reference: class_list_class (table: class_list)
--ALTER TABLE class_list ADD CONSTRAINT class_list_class FOREIGN KEY class_list_class (class_id)
--    REFERENCES class (id);
--
---- Reference: class_list_list (table: class_list)
--ALTER TABLE class_list ADD CONSTRAINT class_list_list FOREIGN KEY class_list_list (list_id)
--    REFERENCES list (id);
--
---- Reference: translation_word_translation (table: translation_word)
--ALTER TABLE translation_word ADD CONSTRAINT translation_word_translation FOREIGN KEY translation_word_translation (translation_id)
--    REFERENCES translation (id);
--
---- Reference: translation_word_word (table: translation_word)
--ALTER TABLE translation_word ADD CONSTRAINT translation_word_word FOREIGN KEY translation_word_word (word_id)
--    REFERENCES word (id);
--
---- Reference: user_class_class (table: user_class)
--ALTER TABLE user_class ADD CONSTRAINT user_class_class FOREIGN KEY user_class_class (class_id)
--    REFERENCES class (id);
--
---- Reference: user_class_user (table: user_class)
--ALTER TABLE user_class ADD CONSTRAINT user_class_user FOREIGN KEY user_class_user (user_id)
--    REFERENCES user (id);
--
---- Reference: user_role (table: user)
--ALTER TABLE user ADD CONSTRAINT user_role FOREIGN KEY user_role (role_id)
--    REFERENCES role (id);
--
---- Reference: word_list_list (table: word_list)
--ALTER TABLE word_list ADD CONSTRAINT word_list_list FOREIGN KEY word_list_list (list_id)
--    REFERENCES list (id);
--
---- Reference: word_list_word (table: word_list)
--ALTER TABLE word_list ADD CONSTRAINT word_list_word FOREIGN KEY word_list_word (word_id)
--    REFERENCES word (id);
--
---- End of file.

INSERT INTO user (username, passwd_hash, first_name, last_name, email, role_id) 
	VALUES ("Pouet", "14b10468a32dbd4d2be8c996930948818cb1ebdb", "Laureline", "Polli", "polli.laureline@destael.educanet2.ch", 1);

INSERT INTO user (username, passwd_hash, first_name, last_name, email, role_id) 
	VALUES ("RaptorDelta999", "14b10468a32dbd4d2be8c996930948818cb1ebdb", "Damien", "Rupp", "rupp.damien@destael.educanet2.ch", 1);

INSERT INTO user (username, passwd_hash, first_name, last_name, email, role_id) 
	VALUES ("LAURELINE", "14b10468a32dbd4d2be8c996930948818cb1ebdb", "Laureline", "POLLI", "lpolli2001@gmail.com", 2);

INSERT INTO user (username, passwd_hash, first_name, last_name, email, role_id) 
	VALUES ("DAMIEN.R", "14b10468a32dbd4d2be8c996930948818cb1ebdb", "Damien", "RUPP", "drupp2001@gmail.com", 2);
