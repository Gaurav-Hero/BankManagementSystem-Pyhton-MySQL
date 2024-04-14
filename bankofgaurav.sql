CREATE DATABASE BankOfGaurav;
USE BankOfGaurav;
CREATE TABLE AccountInfo (
    FullName Varchar(255),
    UID_Number INT NOT NULL,
    PAN_Number Varchar(255),
    City Varchar(255),
    PassKey Varchar(255),
    UserName Varchar(255),
    PRIMARY KEY (UserName)
);
ALTER TABLE AccountInfo
MODIFY COLUMN UID_Number BIGINT;

ALTER TABLE AccountInfo
MODIFY COLUMN UID_Number INT UNSIGNED; -- Change data type and constraints as needed


CREATE TABLE LoginInfo (
    UserName Varchar(255),
    PassKey Varchar(255)
);



select * from `aloo8@banksys`;
select * from AccountInfo;
select * from LoginInfo;
select * from BankMoney;
SET SQL_SAFE_UPDATES = 0;

DELETE FROM LoginInfo;

DROP TABLE `hero22@banksys`;



