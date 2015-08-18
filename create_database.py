#!/usr/bin/env python
# coding=utf-8
import MySQLdb
passwd = '111111'
conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = passwd,port = 3306)
cursor = conn.cursor()
cursor.execute('create database if not exists password CHARACTER SET utf8')
conn.select_db('password');
cursor.close(); 
