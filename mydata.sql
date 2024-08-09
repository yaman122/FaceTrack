show databases;
use mydata;

CREATE TABLE register (
    fname VARCHAR(255) NOT NULL,
    lname VARCHAR(255),
    contact VARCHAR(15),
    email VARCHAR(255) NOT NULL,
    securityQ VARCHAR(255),
    security_A VARCHAR(255),
    confpass VARCHAR(255) NOT NULL
);

select * from register;