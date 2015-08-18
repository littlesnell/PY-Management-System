#!/usr/bin/env python
# coding=utf-8


import re
import MySQLdb
import threading
from socket import *
from time import ctime
from hong import PORT
from hong import BUFSIZ
from hong import ADDR

#ss = socket()
HOST = ''
PORT
def main():
    tcpSerSock = socket(AF_INET,SOCK_STREAM)# 创建一个套接字

    #ss.bind()
    tcpSerSock.bind(ADDR)# 绑定主机号，IP到套接字

    #ss.listen()
    tcpSerSock.listen(5)# 监听数量最多为5
    
    while True:  
        #服务器套接字通过socket的accept方法等待客户请求一个连接
        try:
            print 'waiting for connection...'
            tcpCliSock,addr = tcpSerSock.accept()
            t = threading.Thread(target=tcplink_server, args=(tcpCliSock, addr))
            t.start()
            print '...connected from:',addr
            print 'start at:',ctime()
        except KeyboardInterrupt:
            print '程序结束'
            exit(0)
    tcpSerSock.close()

def tcplink_server(tcpCliSock,addr):#建立多线程
    while True:
        chooce_server(tcpCliSock,addr)
    tcpCliSock.close()

def chooce_server(tcpCliSock,addr):
    a = tcpCliSock.recv(BUFSIZ)
    if a[8:] == '2' and a[0:8] == 'chooce1:':
        tcpCliSock.send('正常退出!')
        tcpCliSock.close()
        print 'Connection from %s:%s closed.' % addr
        print 'waiting for connection...'
        exit(0)
    else:
        if a[0:8] == 'chooce1:':
            tcpCliSock.send('接收成功!')
            a = a[8:]
            if a == '0':
                regidter_server(tcpCliSock,addr)
            if a == '1':
                log_in_server(tcpCliSock,addr)
        else:
            tcpCliSock.send('接收失败!')
            tcpCliSock.close()
            exit(0)


        #if data == 'exit' or not data:
         #   break


def regidter_server(tcpCliSock,addr):#注册类别选择
    b = tcpCliSock.recv(BUFSIZ)
    if b[0:8] =='chooce2:':
        tcpCliSock.send('接收成功!')
        b = b[8:]
        if b == '0':
            student_regidter_server(tcpCliSock,addr)
        if b == '1':
            teacher_regidter_server(tcpCliSock,addr)
    else:
        tcpCliSock.send('接收失败!')
        tcpCliSock.close()
        exit(0)

def log_in_server(tcpCliSock,addr):#登陆选择
    c = tcpCliSock.recv(BUFSIZ)
    if c[0:8] == 'chooce3:':
        tcpCliSock.send('接收成功!')
        #print c
        c = c[8:]
        #print c
        if c == '0':
            student_log_in_server(tcpCliSock,addr)
        if c == '1':
            teacher_log_in_server(tcpCliSock,addr)
    else:
        tcpCliSock.send('接收失败!')
        tcpCliSock.close()
        exit(0)

def student_log_in_server(tcpCliSock,addr):#学生登陆
    conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = '111111',db = 'password',port = 3306,charset = 'utf8')
    cursor = conn.cursor()
    name_server = tcpCliSock.recv(BUFSIZ)
    #print name_server
    #print 'name_server =%s'%name_server[0:12]
    if name_server[0:12] == 'name_client:':
        tcpCliSock.send('接收成功!')
        #print name_server
        name_server = name_server[12:]
    else:
        tcpCliSock.send('接收失败!')
        tcpCliSock.close()
        exit(0)
    passwd_server = tcpCliSock.recv(BUFSIZ)
    #print passwd_server[0:14]
    if passwd_server[0:14] == 'passwd_client:':
        tcpCliSock.send('接收成功!')
        #print passwd_server
        passwd_server = passwd_server[14:]
    else:
        tcpCliSock.send('接收失败!')
        tcpCliSock.close()
        exit(0)
    if (cursor.execute('SELECT * FROM user WHERE name = %s AND password = %s',[name_server,passwd_server])):
        tcpCliSock.send('登陆成功!')
        menu_student_server(tcpCliSock,addr)
    else:
        tcpCliSock.send('登陆失败!')
        chooce_server(tcpCliSock,addr)
        #tcpCliSock.close()

        #exit(0)



def teacher_log_in_server(tcpCliSock,addr):#教师登陆
    conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = '111111',db = 'password',port = 3306,charset = 'utf8')
    cursor = conn.cursor()
    name_server = tcpCliSock.recv(BUFSIZ)
    #print name_server
    #print 'name_server =%s'%name_server[0:12]
    if name_server[0:12] == 'name_client:':
        tcpCliSock.send('接收成功!')
        #print name_server
        name_server = name_server[12:]
    else:
        tcpCliSock.send('接收失败!')
        tcpCliSock.close()
        exit(0)
    passwd_server = tcpCliSock.recv(BUFSIZ)
    #print passwd_server[0:14]
    if passwd_server[0:14] == 'passwd_client:':
        tcpCliSock.send('接收成功!')
        #print passwd_server
        passwd_server = passwd_server[14:]
    else:
        tcpCliSock.send('接收失败!')
        tcpCliSock.close()
        exit(0)
    if (cursor.execute('SELECT * FROM user WHERE name = %s AND password = %s',[name_server,passwd_server])):
        tcpCliSock.send('登陆成功!')
        menu_teacher_server(tcpCliSock,addr)
    else:
        tcpCliSock.send('登陆失败!')
        chooce_server(tcpCliSock,addr)
        #tcpCliSock.close()
        #exit(0)





def student_regidter_server(tcpCliSock,addr):#学生注册
    name = tcpCliSock.recv(BUFSIZ)
    #print name[5:]
    if name[0:5] == 'name:':
        tcpCliSock.send('用户名接收成功!')
        name = name[5:]
        #print 'name = %s'%name
        passwd =tcpCliSock.recv(BUFSIZ)
        if passwd[0:7] == 'passwd:':
            tcpCliSock.send('密码接收成功!')
            passwd = passwd[7:]
         #   print 'passwd = %s'%passwd
            student_connect_server(name,passwd,tcpCliSock,addr)
        else:
            tcpCliSock.send('密码接收失败!')
            tcpSerSock.close()
            exit(0)
    else:
        tcpCliSock.send('用户名接收失败!')
        tcpSerSock.close()
        exit(0)


def teacher_regidter_server(tcpCliSock,addr):#教师注册
    name = tcpCliSock.recv(BUFSIZ)
    #print name[5:]
    if name[0:5] == 'name:':
        tcpCliSock.send('用户名接收成功!')
        name = name[5:]
        #print 'name = %s'%name

        passwd =tcpCliSock.recv(BUFSIZ)
        if passwd[0:7] == 'passwd:':
            tcpCliSock.send('密码接收成功!')
            passwd = passwd[7:]
            #print 'passwd = %s'%passwd

            command = tcpCliSock.recv(BUFSIZ)
            #print command
            #print command[0:8]
            #print command[8:]
            if command[0:8] == 'command:' and command[8:] == 'teacher':
                tcpCliSock.send('口令接收成功!')
                teacher_connect_server(name,passwd,tcpCliSock,addr)
            else:
                tcpCliSock.send('口令接收错误!')
                tcpCliSock.close()
                exit(0)

        else:
            tcpCliSock.send('密码接收失败!')
            tcpSerSock.close()
            exit(0)

    else:
        tcpCliSock.send('用户名接收失败!')
        tcpSerSock.close()
        exit(0)



def student_connect_server(name,passwd,tcpCliSock,addr):#学生连接数据库
    passwd1 = passwd
    #print 'passwd1 = %s'%passwd1
    conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = '111111',db = 'password',port = 3306,charset = 'utf8')
    cursor = conn.cursor()
    student_write_server(name,passwd1,conn,cursor,tcpCliSock,addr)






def teacher_connect_server(name,passwd1,tcpCliSock,addr):#教师连接数据库
    conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = '111111',db = 'password',port = 3306 ,charset = 'utf8')
    cursor = conn.cursor()
    teacher_write_server(name,passwd1,conn,cursor,tcpCliSock,addr)






def teacher_write_server(name,passwd1,conn,cursor,tcpCliSock,addr):#教师注册结果
    if (cursor.execute('INSERT INTO user1 (name,password)VALUES (%s,%s)',[name,passwd1])):
        tcpCliSock.send('注册成功!')
    else:
        tcpCliSock.send('注册失败!')
    conn.commit()
    conn.close()




def student_write_server(name,passwd1,conn,cursor,tcpCliSock,addr):#学生注册结果
    if (cursor.execute('INSERT INTO user (name,password) VALUES (%s,%s)',[name,passwd1])):
        tcpCliSock.send('注册成功!')
    else:
        tcpCliSock.send('注册失败!')
    conn.commit()
    conn.close()

def menu_student_server(tcpCliSock,addr):#学生菜单
    d = 'd:''-1'
    while d[2:] != '2':
        d = tcpCliSock.recv(BUFSIZ)
        #print d
        if d[2:] == '2' and d[0:2] == 'd:':
            tcpCliSock.send('正常退出!')
            tcpCliSock.close()
            print 'Connection from %s:%s closed.' % addr
            print 'waiting for connection...'
            exit(0)
        else:
            if d[0:2] == 'd:':
                tcpCliSock.send('发送成功!')
                d = d[2:]
                #print d
                if d == '1':
                    score_select_server(tcpCliSock)
            else:
                tcpCliSock.send('发送失败!')
                tcpCliSock.close()
                exit(0)
     

def score_select_server(tcpCliSock):#学生查询类别选择
    e = tcpCliSock.recv(BUFSIZ)
    #print e
    if e[0:2] == 'e:':
        tcpCliSock.send('接收成功!')
        e = e[2:]
        #print 'e = %s'%e
        conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = '111111',db = 'password',port = 3306 ,charset = 'utf8')
        cursor = conn.cursor()
        if e == '1':
            #print '按学号查询'
            number = tcpCliSock.recv(BUFSIZ)
            #print 'number = %s'%number
            if number[0:7] == 'number:':
                tcpCliSock.send('number接收成功!')
                number = number[7:]
            else:
                tcpCliSock.send('number接收失败!')
                tcpCliSock.close()
                exit(0)
            if (cursor.execute('SELECT * FROM  score WHERE number = %s'%number)):
                tcpCliSock.send('查询成功!\n')
                values = cursor.fetchone()
                s = values[0].encode('utf-8')
                s1 = values[1].encode('utf-8')
                s2 = values[2].encode('utf-8')
                s3 = str(values[3])
                s4 = str(values[4])
                s5 = str(values[5])
                s6 = str(values[6])
                s7 = '%s'%s + ',%s'%s1 + ',%s'%s2 + ',%s'%s3 + ',%s'%s4 + ',%s'%s5 + ',%s'%s6
                #print type(s7)
                #print 's7'
                tcpCliSock.send(s7)
            else:
                tcpCliSock.send('查询失败!')
                tcpCliSock.close()
                exit(0)



        if e == '2':
            #print '按姓名查询'
            name = tcpCliSock.recv(BUFSIZ)
            #print 'name = %s'%name
            if name[0:5] == 'name:':
                tcpCliSock.send('name接收成功!')
                name = name[5:]
                #print type(name)
                #print 'name'
            else:
                tcpCliSock.send('name接受失败!')
                tcpCliSock.close()
                exit(0)
            if (cursor.execute('SELECT * FROM  score WHERE name = %s',name)):
                tcpCliSock.send('查询成功!\n')
                values = cursor.fetchall()
                m = cursor.rowcount
                cursor.rowcount = str(cursor.rowcount)
                #tcpCliSock.send(cursor.rowcount)
                #count = tcpCliSock.recv(BUFSIZ)
                s = [['',]*7]*m
                s2 = ['',]*m
                for j in range(m):
                    #print 'j = %s'%j
                    #print 'm = %s'%m
                    for i in range(7):
                        #print i
                        s[j][i] = str(s[j][i])
                        if i <= 2:
                            s[j][i] = values[j][i].encode('utf-8')
                            #print s[j][i]
                            #print 's[j][i]'
                        if 2 < i and i <= 6:
                            s[j][i] = str(values[j][i])
                            #print s[j][i]
                            #print 's[j][i]'
                    #for i in range(7):
                        #print s[j][i]
                        #print '\n'
                    s2[j] = '%s'%s[j][0] + ',%s'%s[j][1] + ',%s'%s[j][2] + ',%s'%s[j][3] + ',%s'%s[j][4] + ',%s'%s[j][5] + ',%s\n'%s[j][6]
                    #print type(s2[j])
                    #print 's2'
                    tcpCliSock.send(s2[j])
            else:
                tcpCliSock.send('查询失败!')
                tcpCliSock.close()
                exit(0)
    else:
        tcpCliSock.send('发送失败!')
        tcpCliSock.close()
        exit(0)




def menu_teacher_server(tcpCliSock,addr):#教师类别选择
    g = 'g:''-1'
    while g[2:] != '5':
        g = tcpCliSock.recv(BUFSIZ)
        #print g
        if g[2:] == '5' and g[0:2] == 'g:':
            tcpCliSock.send('正常退出!')
            tcpCliSock.close()
            print 'Connection from %s:%s closed.' % addr
            print 'waiting for connection...'
            exit(0)
        else:
            if g[0:2] == 'g:':
                tcpCliSock.send('发送成功!')
                g = g[2:]
                #print g
                if g == '1':
                    score_select_server(tcpCliSock)
                if g == '2':
                    score_add_server(tcpCliSock)
                if g == '3':
                    score_delete_server(tcpCliSock)
                if g == '4':
                    score_update_server(tcpCliSock)
            else:
                tcpCliSock.send('发送失败!')
                tcpCliSock.close()
                exit(0)



def score_add_server(tcpCliSock):#成绩添加
    conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = '111111',db = 'password',port = 3306 ,charset = 'utf8')
    cursor = conn.cursor()
    add = tcpCliSock.recv(BUFSIZ)
    #print add
    add = add.split(',')
    name = add[0]
    #print type(name)
    number = add[1]
    classes = add[2]
    #print type(classes)
    age = add[3]
    english = add[4]
    chinese = add[5]
    math = add[6]
    if (cursor.execute('INSERT INTO score (name,number,class,age,english,chinese,math) values (%s,%s,%s,%s,%s,%s,%s)',[name,number,classes,age,english,chinese,math])):
        tcpCliSock.send('增添成功!')
    else:
        tcpCliSock.send('增添失败!')
        tcpCliSock.close()
        exit(0)
    conn.commit()
    conn.close()


def score_delete_server(tcpCliSock):#成绩删除
    conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = '111111',db = 'password',port = 3306 ,charset = 'utf8')
    cursor = conn.cursor()
    if (cursor.execute('SELECT * FROM  score')):
        tcpCliSock.send('查询成功!\n')
        values = cursor.fetchall()
        m = cursor.rowcount
        cursor.rowcount = str(cursor.rowcount)
        s = [['',]*7]*m
        s2 = ['',]*m
        for j in range(m):
            #print 'j = %s'%j
            #print 'm = %s'%m
            for i in range(7):
                #print i
                s[j][i] = str(s[j][i])
                if i <= 2:
                    s[j][i] = values[j][i].encode('utf-8')
                    #print s[j][i]
                    #print 's[j][i]'
                if 2 < i and i <= 6:
                    s[j][i] = str(values[j][i])
                    #print s[j][i]
                    #print 's[j][i]'
            #for i in range(7):
                #print s[j][i]
                #print '\n'
            s2[j] = '%s'%s[j][0] + ',%s'%s[j][1] + ',%s'%s[j][2] + ',%s'%s[j][3] + ',%s'%s[j][4] + ',%s'%s[j][5] + ',%s\n'%s[j][6]
            #print type(s2[j])
            #print 's2'
            tcpCliSock.send(s2[j])
    else:
        tcpCliSock.send('查询失败!')
        tcpCliSock.close()
        exit(0)
    number = tcpCliSock.recv(BUFSIZ)
    if number[0:7] == 'number:':
        tcpCliSock.send('接收成功!')
        number = number[7:]
        if(cursor.execute('DELETE FROM score WHERE number = %s',number)):
            tcpCliSock.send('删除成功!')
        else:
            tcpCliSock.send('删除失败!')
            tcpCliSock.close()
            exit(0)
        conn.commit()
        conn.close()
    else:
        tcpCliSock.send('接收失败!')
        tcpCliSock.close()
        exit(0)






def score_update_server(tcpCliSock):#成绩修改
    conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = '111111',db = 'password',port = 3306 ,charset = 'utf8')
    cursor = conn.cursor()
    if (cursor.execute('SELECT * FROM  score')):
        tcpCliSock.send('查询成功!\n')
        values = cursor.fetchall()
        m = cursor.rowcount
        cursor.rowcount = str(cursor.rowcount)
        s = [['',]*7]*m
        s2 = ['',]*m
        for j in range(m):
            #print 'j = %s'%j
            #print 'm = %s'%m
            for i in range(7):
                #print i
                s[j][i] = str(s[j][i])
                if i <= 2:
                    s[j][i] = values[j][i].encode('utf-8')
                    #print s[j][i]
                    #print 's[j][i]'
                if 2 < i and i <= 6:
                    s[j][i] = str(values[j][i])
                    #print s[j][i]
                    #print 's[j][i]'
            #for i in range(7):
                #print s[j][i]
                #print '\n'
            s2[j] = '%s'%s[j][0] + ',%s'%s[j][1] + ',%s'%s[j][2] + ',%s'%s[j][3] + ',%s'%s[j][4] + ',%s'%s[j][5] + ',%s\n'%s[j][6]
            #print type(s2[j])
            #print 's2'
            tcpCliSock.send(s2[j])
    else:
        tcpCliSock.send('查询失败!')
        tcpCliSock.close()
        exit(0)
    number = tcpCliSock.recv(BUFSIZ)
    if number[0:7] == 'number:':
        tcpCliSock.send('number接收成功!')
        number = number[7:]
    else:
        tcpCliSock.send('number接收失败!')
        tcpCliSock.close()
        exit(0)
    subject = tcpCliSock.recv(BUFSIZ)
    if subject[0:8] == 'subject:':
        tcpCliSock.send('subject接收成功!')
        subject = subject[8:]
    else:
        tcpCliSock.send('subject接收失败!')
        tcpCliSock.close()
        exit(0)
    information = tcpCliSock.recv(BUFSIZ)
    if information[0:12] == 'information:':
        tcpCliSock.send('information接收成功!')
        information = information[12:]
        if subject == 'name':
            if(cursor.execute('update score set name = %s WHERE number = %s',[information,number])):
                tcpCliSock.send('修改信息成功!')
            else:
                tcpCliSock.send('修改信息失败!')
                tcpCliSock.close()
                exit(0)

        if subject == 'number':
            if(cursor.execute('update score set number = %s WHERE number = %s',[information,number])):
                tcpCliSock.send('修改信息成功!')
            else:
                tcpCliSock.send('修改信息失败!')
                tcpCliSock.close()
                exit(0)

        if subject == 'class':
            if(cursor.execute('update score set class = %s WHERE number = %s',[information,number])):
                tcpCliSock.send('修改信息成功!')
            else:
                tcpCliSock.send('修改信息失败!')
                tcpCliSock.close()
                exit(0)
        if subject == 'age':
            if(cursor.execute('update score set age = %s WHERE number = %s',[information,number])):
                tcpCliSock.send('修改信息成功!')
            else:
                tcpCliSock.send('修改信息失败!')
                tcpCliSock.close()
                exit(0)
        if subject == 'english':
            if(cursor.execute('update score set english = %s WHERE number = %s',[information,number])):
                tcpCliSock.send('修改信息成功!')
            else:
                tcpCliSock.send('修改信息失败!')
                tcpCliSock.close()
                exit(0)
        if subject == 'chinese':
            if(cursor.execute('update score set chinese = %s WHERE number = %s',[information,number])):
                tcpCliSock.send('修改信息成功!')
            else:
                tcpCliSock.send('修改信息失败!')
                tcpCliSock.close()
                exit(0)
        if subject == 'math':
            if(cursor.execute('update score set math = %s WHERE number = %s',[information,number])):
                tcpCliSock.send('修改信息成功!')
            else:
                tcpCliSock.send('修改信息失败!')
                tcpCliSock.close()
                exit(0)
        conn.commit()
    else:
        tcpCliSock.send('information接收失败!')
        tcpCliSock.close()
        exit(0)






if __name__ == '__main__':
    main()
