#
# [centos@localhost ~]$ mysql  -h  127.0.0.1  -u  root
#
# Welcome to the MariaDB monitor.  Commands end with ; or \g.
#
# Your MariaDB connection id is 6
#
# Server version: 5.5.60-MariaDB MariaDB Server
#
#
#
#
# Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.
#
#
#
#
# Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
#
#
#
#
# MariaDB [(none)]> exit
#
# Bye
#
# [centos@localhost ~]$ mysql  -h  127.0.0.1  -u  root  -p
#
# Enter password:
#
# Welcome to the MariaDB monitor.  Commands end with ; or \g.
#
# Your MariaDB connection id is 7
#
# Server version: 5.5.60-MariaDB MariaDB Server
#
#
#
#
# Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.
#
#
#
#
# Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
#
#
#
#
# MariaDB [(none)]> SHOW  DATABASES;
#
# +--------------------+
#
# | Database           |
#
# +--------------------+
#
# | information_schema |
#
# | mysql              |
#
# | performance_schema |
#
# | test               |
#
# +--------------------+
#
# 4 rows in set (0.00 sec)
#
#
#
#
# MariaDB [(none)]> CREATE  DATABASE  userDB;
#
# Query OK, 1 row affected (0.00 sec)
#
#
#
#
# MariaDB [(none)]> SHOW  DATABASES;
#
# +--------------------+
#
# | Database           |
#
# +--------------------+
#
# | information_schema |
#
# | mysql              |
#
# | performance_schema |
#
# | test               |
#
# | userDB             |
#
# +--------------------+
#
# 5 rows in set (0.01 sec)
#
#
#
#
# MariaDB [(none)]> USE  userDB;
#
# Database changed
#
# MariaDB [userDB]> CREATE  TABLE  userTable (
#
#     -> userID   CHAR(10),
#
#     -> userName  CHAR(5),
#
#     -> userAge  INT );
#
# Query OK, 0 rows affected (0.01 sec)
#
#
#
#
# MariaDB [userDB]> INSERT INTO userTable VALUES( 'AAA' , 'aaa' , 21 );
#
# Query OK, 1 row affected (0.00 sec)
#
#
#
#
# MariaDB [userDB]> INSERT INTO userTable VALUES( 'BBB' , 'bbb' , 23 );
#
# Query OK, 1 row affected (0.01 sec)
#
#
#
#
# MariaDB [userDB]> INSERT INTO userTable VALUES( 'CCC' , 'ccc' , 35 );
#
# Query OK, 1 row affected (0.00 sec)
#
#
#
#
# MariaDB [userDB]> INSERT INTO userTable VALUES(
#
#     -> ;
#
# ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '' at line 1
#
# MariaDB [userDB]> INSERT INTO userTable VALUES('
#
#     '> '
#
#     -> ;
#
# ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '' at line 1
#
# MariaDB [userDB]> SELECT  *  FROM  userTable;
#
# +--------+----------+---------+
#
# | userID | userName | userAge |
#
# +--------+----------+---------+
#
# | AAA    | aaa      |      21 |
#
# | BBB    | bbb      |      23 |
#
# | CCC    | ccc      |      35 |
#
# +--------+----------+---------+
#
# 3 rows in set (0.01 sec)
#
#
#
#
# MariaDB [userDB]> SELECT  *  FROM  userTable WHERE  userID = 'AAA';
#
# +--------+----------+---------+
#
# | userID | userName | userAge |
#
# +--------+----------+---------+
#
# | AAA    | aaa      |      21 |
#
# +--------+----------+---------+
#
# 1 row in set (0.01 sec)
#
#
#
#
# MariaDB [userDB]> SELECT  *  FROM  userTable WHERE  userAge < 30;
#
# +--------+----------+---------+
#
# | userID | userName | userAge |
#
# +--------+----------+---------+
#
# | AAA    | aaa      |      21 |
#
# | BBB    | bbb      |      23 |
#
# +--------+----------+---------+
#
# 2 rows in set (0.00 sec)
#
#
#
#
# MariaDB [userDB]> SELECT  userName  FROM  userTable WHERE  userAge < 30;
#
# +----------+
#
# | userName |
#
# +----------+
#
# | aaa      |
#
# | bbb      |
#
# +----------+
#
# 2 rows in set (0.00 sec)
#
#
#
#
# MariaDB [userDB]> SELECT  userName.userAge  FROM  userTable WHERE  userAge < 30;
#
# ERROR 1054 (42S22): Unknown column 'userName.userAge' in 'field list'
#
# MariaDB [userDB]> SELECT  userName,userAge  FROM  userTable WHERE  userAge < 30;
#
# +----------+---------+
#
# | userName | userAge |
#
# +----------+---------+
#
# | aaa      |      21 |
#
# | bbb      |      23 |
#
# +----------+---------+
#
# 2 rows in set (0.00 sec)
#
#
#
#
# MariaDB [userDB]> exit
#
# Bye



