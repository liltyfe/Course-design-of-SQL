# 创建学生数据库

CREATE DATABASE studentdb;

USE studentdb;

# 创建用户表
CREATE TABLE users (
  username VARCHAR(50) PRIMARY KEY,
  passwords VARCHAR(20) UNIQUE
);

# 添加用户
INSERT INTO users (username, passwords) VALUES ('admin', '123456') , ('teacher', '456123');

DESC users;

SELECT * FROM users;


# 创建学生表
CREATE TABLE students(
	stname VARCHAR(50),
	stID INT PRIMARY KEY,
	mathsc INT,
	chinesessc INT,
	englishse INT
);

DESC students;

SELECT * FROM students;




