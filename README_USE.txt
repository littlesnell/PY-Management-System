这部分主要想说的的如何使用这个查询系统（python），我仍然只是个新手，存在的问题请大神指出。
首先我使用了数据库。
如何创建一个能让这个程序使用的数据库。首先将create_dadabase.py和create_table.py两个文件放在一块，用python运行create_table.py。创建并且生出3个表，分别是user，user1，score。
user中的内容是学生注册的信息。
user1中的内容是教师注册的信息，口令为teacher。
score中存储的是需要增删改查的学生信息，可以使用my.sql增添数据（如果嫌麻烦的话）,可以自己往里添加数据。

使用的话有明显的提示，先运行tsTserv.py，在运行tsTclnt.py，可以运行多个tsTclnt.py。
hong.py是服务器中存储的IP，PORT等，可以进行修改，修改后记着修改客户端的该内容。
可以私网的使用，程序的问题记者告诉我啊，亲！
