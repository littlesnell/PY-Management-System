#!/usr/bin/env python
# coding=utf-8


from socket import *
#from hong import HOST
#from hong import PORT
#from hong import BUFSIZ
#from hong import ADDR
#from time import sleep

HOST = raw_input('请输入服务器的IP地址:')
BUFSIZ = 1024
PORT = 20000
ADDR = (HOST,PORT)
def main():
    tcpCliSock = socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    while True:
        if(chooce_client(tcpCliSock)):#调用用户登陆界面
            menu_client()
       # data = raw_input('> ')
        if not data:
            break
        if data == 'exit':
            break
        tcpCliSock.send(data)
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print data
    tcpCliSock.send('exit')
    tcpCliSock.close()


def chooce_client(tcpCliSock):#用户选择
    a = -1
    while a != '2':
        print '0-用户注册'
        print '1-用户登陆'
        print '2-退出'
        a = raw_input('请输入你的选择:')
        a = 'chooce1:''%s'%a
        tcpCliSock.send(a)
        aout = tcpCliSock.recv(BUFSIZ)
        print aout#接收成功
        a = a[8:]
        if a == '0':
            regidter_client(tcpCliSock)
        elif a == '1':
            log_in_client(tcpCliSock)
        elif a == '2':
            resultout = tcpCliSock.recv(BUFSIZ)
            print resultout
            exit(0)
        else:
            print '输入错误!'





def regidter_client(tcpCliSock):#注册类别选择
    print '0-学生注册'
    print '1-教师注册'
    b = raw_input('请输入你的选择:')
    b = 'chooce2:''%s'%b
    tcpCliSock.send(b)
    result1out = tcpCliSock.recv(BUFSIZ)
    print result1out
    b = b[8:]
    #print b
    if b == '0':
        student_regidter_client(tcpCliSock)
    if b == '1':
        teacher_regidter_client(tcpCliSock)



def log_in_client(tcpCliSock):#登陆选择
    print '0-学生登陆'
    print '1-教师登陆'
    c = raw_input('请输入你的选择:')
    c = 'chooce3:''%s'%c
    #print c
    tcpCliSock.send(c)
    result2out = tcpCliSock.recv(BUFSIZ)
    print result2out
    c = c[8:]
    #print c
    if c == '0':
        student_log_in_client(tcpCliSock)
    if c =='1':
        teacher_log_in_client(tcpCliSock)



def student_log_in_client(tcpCliSock):#学生登陆
    name_client = raw_input('姓名:')
    name_client = 'name_client:''%s'%name_client
    #print name_client
    passwd_client = raw_input('密码:')
    passwd_client ='passwd_client:''%s'%passwd_client
    #print passwd_client
    tcpCliSock.send(name_client)
    name_clientout = tcpCliSock.recv(BUFSIZ)
    print name_clientout
    tcpCliSock.send(passwd_client)
    passwd_clientout = tcpCliSock.recv(BUFSIZ)
    print passwd_clientout
    student_log_in_clientout = tcpCliSock.recv(BUFSIZ)
    print student_log_in_clientout
    if student_log_in_clientout == '登陆成功!':
        menu_student_client(tcpCliSock)



def teacher_log_in_client(tcpCliSock):#教师登陆
    name_client = raw_input('姓名:')
    name_client = 'name_client:''%s'%name_client
    #print name_client
    passwd_client = raw_input('密码:')
    passwd_client ='passwd_client:''%s'%passwd_client
    #print passwd_client
    tcpCliSock.send(name_client)
    name_clientout = tcpCliSock.recv(BUFSIZ)
    print name_clientout
    tcpCliSock.send(passwd_client)
    passwd_clientout = tcpCliSock.recv(BUFSIZ)
    print passwd_clientout
    teacher_log_in_clientout = tcpCliSock.recv(BUFSIZ)
    print teacher_log_in_clientout
    if teacher_log_in_clientout == '登陆成功!':
        menu_teacher_client(tcpCliSock)




def student_regidter_client(tcpCliSock):#学生注册
    name = raw_input('用户名:')
    name = 'name:''%s'%name
    passwd = raw_input('密码:')
    passwd = 'passwd:''%s'%passwd
    enter_passwd = raw_input('确认密码:')
    enter_passwd = 'passwd:''%s'%enter_passwd
    if passwd != enter_passwd:
        print '输入密码不一致，请重新输入!'
    else:
        tcpCliSock.send(name)
        nameout = tcpCliSock.recv(BUFSIZ)
        print nameout
        tcpCliSock.send(passwd)
        passwdout = tcpCliSock.recv(BUFSIZ)
        print passwdout
        student_connect_client(name,passwd,tcpCliSock)


def student_connect_client(name,passwd,tcpCliSock):#学生连接数据库
    student_write_client(name,passwd,tcpCliSock)




def teacher_regidter_client(tcpCliSock):#教师注册
    name = raw_input('用户名:')
    name = 'name:''%s'%name
    passwd = raw_input('密码:')
    passwd = 'passwd:''%s'%passwd
    enter_passwd = raw_input('确认密码:')
    enter_passwd = 'passwd:''%s'%enter_passwd
    command = raw_input('口令:')
    command = 'command:''%s'%command
    if passwd != enter_passwd:
        print '输入密码不一致，请重新输入!'
    else:
        tcpCliSock.send(name)
        nameout = tcpCliSock.recv(BUFSIZ)
        print nameout
        tcpCliSock.send(passwd)
        passwdout = tcpCliSock.recv(BUFSIZ)
        print passwdout
        tcpCliSock.send(command)
        commandout = tcpCliSock.recv(BUFSIZ)
        print commandout
        teacher_connect_client(name,passwd,tcpCliSock)

def teacher_connect_client(name,passwd,tcpCliSock):#教师连接数据库
    teacher_write_client(name,passwd,tcpCliSock)

def teacher_write_client(name,passwd,tcpCliSock):#教师注册结果
    teacher_writeout = tcpCliSock.recv(BUFSIZ)
    print teacher_writeout


def student_write_client(name,passwd,tcpCliSock):#学生注册结果
    student_writeout = tcpCliSock.recv(BUFSIZ)
    print student_writeout


def menu_student_client(tcpCliSock):#学生菜单
    d = -1#修改
    while d != '2':
        print '1-成绩查询'
        print '2-退出'
        d = raw_input('请输入你的选择:')
        d = 'd:''%s'%d
        tcpCliSock.send(d)
        dout = tcpCliSock.recv(BUFSIZ)
        print dout
        d = d[2:]
        if d == '1':
            score_select_client(tcpCliSock)
        if d == '2':
            result3out = tcpCliSock.recv(BUFSIZ)
            print result3out
            exit(0)
       


def score_select_client(tcpCliSock):#学生查询类别选择
    print '1-按学号查询'
    print '2-按姓名查询'
    e = raw_input('请输入你的选择:')
    if e == '1':
        number = raw_input('请输入需要查询的学号:')
        number = 'number:''%s'%number
        e = 'e:''%s'%e
        tcpCliSock.send(e)
        eout = tcpCliSock.recv(BUFSIZ)
        print eout
        tcpCliSock.send(number)
        numberout = tcpCliSock.recv(BUFSIZ)
        print numberout
        score_select_clientout = tcpCliSock.recv(BUFSIZ)
        print score_select_clientout
    if e == '2':
        name = raw_input('请输入需要查询的姓名:')
        name = 'name:''%s'%name
        e ='e:''%s'%e
        tcpCliSock.send(e)
        eout = tcpCliSock.recv(BUFSIZ)
        print eout
        tcpCliSock.send(name)
        nameout = tcpCliSock.recv(BUFSIZ)
        print nameout
        score_select_clientout = tcpCliSock.recv(BUFSIZ)
        print score_select_clientout
        #score_select_clientout = tcpCliSock.recv(BUFSIZ)
        #print score_select_clientout

def menu_teacher_client(tcpCliSock):#教师类别选择
    g = -1#修改
    while g != 5:
        print '1-成绩查询'
        print '2-增添成绩'
        print '3-删除成绩'
        print '4-成绩修改'
        print '5-退出'
        g = raw_input('请输入你的选择:')
        g = 'g:''%s'%g
        tcpCliSock.send(g)
        gout = tcpCliSock.recv(BUFSIZ)
        print gout
        g = g[2:]
        if g == '1':
            score_select_client(tcpCliSock)
        if g == '2':
            score_add_client(tcpCliSock)
        if g == '3':
            score_delete_client(tcpCliSock)
        if g == '4':
            score_update_client(tcpCliSock)
        if g == '5':
            result3out = tcpCliSock.recv(BUFSIZ)
            print result3out
            exit(0)


def score_add_client(tcpCliSock):#成绩添加
    name = raw_input('name:')
    number = raw_input('number:')
    classes = raw_input('class:')
    age = raw_input('age:')
    english = raw_input('english:')
    chinese = raw_input('chinese:')
    math = raw_input('math:')
    add = '%s'%name + ',%s'%number + ',%s'%classes + ',%s'%age + ',%s'%english + ',%s'%chinese + ',%s'%math
    #print add
    tcpCliSock.send(add)
    addout = tcpCliSock.recv(BUFSIZ)
    print addout



def score_delete_client(tcpCliSock):#成绩删除
    selectout = tcpCliSock.recv(BUFSIZ)
    print selectout
    number = raw_input('请输入需要删除的学号:')
    number = 'number:''%s'%number
    #print number
    tcpCliSock.send(number)
    numberout = tcpCliSock.recv(BUFSIZ)
    print numberout
    deleteout = tcpCliSock.recv(BUFSIZ)
    print deleteout
   

def score_update_client(tcpCliSock):#成绩修改
    selectout = tcpCliSock.recv(BUFSIZ)
    print selectout
    number = raw_input('请输入需要修改学生的学号:')
    number = 'number:''%s'%number
    #print number
    tcpCliSock.send(number)
    numberout = tcpCliSock.recv(BUFSIZ)
    print numberout
    print '类别有:name,number,class,age,english,chinese,math'
    subject = raw_input('请输入需要修改信息的类别:')
    subject = 'subject:''%s'%subject
    tcpCliSock.send(subject)
    subjectout = tcpCliSock.recv(BUFSIZ)
    print subjectout
    information = raw_input('请输入需要修改信息为:')
    information = 'information:''%s'%information
    print information
    tcpCliSock.send(information)
    informationout = tcpCliSock.recv(BUFSIZ)
    print informationout

if __name__ == '__main__':
    main()
