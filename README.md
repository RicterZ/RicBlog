RicBlog
=======

##更新计划

    TimeLine方法
    RSS订阅

##Introduction
This is a lightweight blog system.   
It is written in Python.   
It is beautiful and elegant.   

    Version  : 0.1.1 - 2013/10/21
    Author   : Ricter (@RicterZ)
    Website  : http://www.ricter.info
    E-mail   : RicterZheng@gmail.com
    Frame: Jinja2, Web.py, Bootstrap, Markdown

RicBlog是一个轻量级博客系统。   
它是由Python编写的。   
它是美丽并且优雅的。   
为了最简洁，它尽量少用try...except   
为了最简洁，它把所有错误处理交给系统   

    DataBase : MySQL
    Python   : Python2
    Other: uwsgi(not necessary)
    Setting  :

###Template path

    eg.templates_path = 'templates'
    MySQL DataBase
    eg.MySQL_host       = 'www.ricter.info'
       MySQL_user       = 'root'
       MySQL_pass       = '123456'
       MySQL_DB         = 'myblog'
       MySQL_blog_table = 'blog'
       MySQL_user_table = 'user'

###Blog Title

    eg.default_title = ' | RicterZ's Blog | Welcome!'
    PS:#中文需要加上 '.decode("gbk")'

###Blog Manager

    eg.blog_bacground_user = 'admin'
       blog_bacground_pass = 'admin'

###MySQL DataBase Structure

    -  blog
    -------------
    id A_I, int
    title  text, gb2312_chinese_ci
    time   text, gb2312_chinese_ci
    contenttext, gb2312_chinese_ci
    lookcount  int
    -  session
    -------------
    sessiontext, gb2312_chinese_ci


