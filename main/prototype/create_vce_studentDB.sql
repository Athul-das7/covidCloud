SET SQL_SAFE_UPDATES = 0;

DROP DATABASE IF EXISTS vce_studentDB;
CREATE DATABASE vce_studentDB;
USE vce_studentDB;

create table student_list (
	roll_no varchar(15) primary key,
    student_name varchar(30) not null,
    branch varchar(5) not null,
    section char not null,
    img_path varchar(28) not null
);

INSERT INTO student_list(roll_no,student_name,branch,section,img_path) VALUE
("1602-19-735-062","JAJALA ABHINAV REDDY","ECE","B","E:\\RollNo\\media\\62.jpg"),
("1602-19-735-063","GUNDETI ADI DEV","ECE","B","E:\\RollNo\\media\\63.jpg"),
("1602-19-735-064","CHILUKURI ADITYA","ECE","B","E:\\RollNo\\media\\64.jpg");

 