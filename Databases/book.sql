-- Creating Database
CREATE DATABASE Stadium;
USE Stadium;


-- Testing Operations
DROP TABLE Book;
DROP TABLE Transactions;
TRUNCATE Book;
TRUNCATE Transactions;
TRUNCATE Stadiums;


-- Vier Operations
SHOW TABLES;
SELECT * from Book;
SELECT * from Transactions;
SELECT * from Stadiums;

DESCRIBE Book;
DESCRIBE Transactions;


-- Table for storing data for bookings done
CREATE TABLE IF NOT EXISTS Book (
    tid INT PRIMARY KEY UNIQUE AUTO_INCREMENT,
    book_time DATETIME NOT NULL,
    show_name VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    event_date DATE NOT NULL,
    attendees INT NOT NULL,
    tier VARCHAR (20) NOT NULL,
    price INT NOT NULL
);

ALTER TABLE Book AUTO_INCREMENT=1001;
ALTER TABLE Book DROP book_time;


-- Transactions table to store each and every transaction (booking and refund)
CREATE TABLE IF NOT EXISTS Transactions (
    tid INT ,
    email VARCHAR(50) NOT NULL,
    refund INT,
    show_name VARCHAR(20) NOT NULL,
    tier VARCHAR (20) NOT NULL,
    event_date DATE NOT NULL,
    amount INT NOT NULL,
    CONSTRAINT PK_transaction PRIMARY KEY (tid, refund)
);


-- Table to store contantly updating information about stadiums and seats
CREATE TABLE IF NOT EXISTS Stadiums (
    name VARCHAR(30) NOT NULL,
    tier VARCHAR (20) NOT NULL,
    seats INT NOT NULL,
    price INT NOT NULL,
    CONSTRAINT PK_transaction PRIMARY KEY (name, tier)
);

ALTER TABLE Stadiums
ADD COLUMN def_no INT NOT NULL;


UPDATE stadiums SET `seats`=100 WHERE name='Sol Colosseum' AND tier='Upper';


-- 
INSERT INTO stadiums
VALUES ('Sol Colosseum', 'Upper', 390, 400, 390);

INSERT INTO stadiums
VALUES ('Sol Colosseum', 'Lower', 650, 600, 650);

INSERT INTO stadiums
VALUES ('Sol Colosseum', 'Ground', 450, 520, 450);

INSERT INTO stadiums
VALUES ('Sol Colosseum', 'Terrace', 240, 470, 240);

INSERT INTO stadiums
VALUES ('Sol Colosseum', 'Hospitality', 100, 690, 100);

-- =======================================================

INSERT INTO stadiums
VALUES ('Domus Flau', 'Upper', 430, 420, 430);

INSERT INTO stadiums
VALUES ('Domus Flau', 'Lower', 680, 620, 680);

INSERT INTO stadiums
VALUES ('Domus Flau', 'Ground', 500, 550, 500);

INSERT INTO stadiums
VALUES ('Domus Flau', 'Terrace', 280, 600, 280);

INSERT INTO stadiums
VALUES ('Domus Flau', 'Hospitality', 125, 730, 125);

-- =======================================================