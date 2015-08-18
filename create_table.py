#!/usr/bin/env python
# coding=utf-8
# 导入MySQL驱动
import MySQLdb
from create_database import passwd
#进行连接数据库
conn = MySQLdb.connect(host="localhost",user="root",passwd=passwd,db="password",port=3306,charset="utf8")
cursor = conn.cursor()
# 创建用户表
#学生注册
cursor.execute('create table user (name varchar(30),password varchar(30))')
#教师注册
cursor.execute('create table user1 (name varchar(30),password varchar(30))')
#成绩数据库
cursor.execute('create table score(name varchar(30),number varchar(30) primary key,class varchar(30),age int(11),english int(11),chinese int(11),math int(11))')
cursor.close()
conn.close()
