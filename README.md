RicBlog
=======

##吐槽
比较奇葩的一个地方是为毛后台密码在程序里数据库就存一个session！   
唔，需要的包如下   

    web.py
    - MySQLDb (web.py需要)
    Jinja2
    markdown

####注意模板中index.html和article.html中有几处地方是要复制Disqus的获取评论数或者获取评论的js的，不要忘了   
写作方式就是markdown写作。RSS那里我不是很熟所以貌似写的很烂。   
实际上写的都很烂....QAQ，大牛勿喷...   
膜拜<a href="http://github.com/whtsky">whtsky</a>大神！   
前端后端都是我自己来的..所以貌似整体都很烂..   
啊，sad story   
 
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
    PS:#这里出现错误的时候就是奇葩中文编码的错误，把decode改成gbk试试

###Blog Manager

    eg.blog_bacground_user = 'admin'
       blog_bacground_pass = 'admin'

###MySQL DataBase Structure

    - blog
    -------------
    id         int ,   A_I
    title      text, gb2312_chinese_ci
    time       text, gb2312_chinese_ci
    content    text, gb2312_chinese_ci
    lookcount  int


    - session
    -------------
    session    text, gb2312_chinese_ci


##RP主机配置

* 首先你要git到RP主机上    
* 切换到RicBlog的目录：`cd RicBlog`   
* 编辑好settings.py之后，注意数据库字段啥的要创建好，运行


     uwsgi --socket /home/[your-RP-ID]/ricblog.sock --wsgi-file main.py --enable-threads


/home/[your-RP-ID]/ricblog.sock是自动生成的，不用管。   
然后不要着急查看效果，跑到RP面板配置一下:

- 绑定的域名，就是你的域名
- 数据源：`/home/[your-RP-ID]/web/RicBlog`
- 站点类型是`uWSGI`
- Socket就是上面的你运行的所填写的`/home/[your-RP-ID]/ricblog.sock`
- Alias别名：`/static/ /home/[your-RP-ID]/web/RicBlog/static/`
RicBlog
=======

##吐槽
比较奇葩的一个地方是为毛后台密码在程序里数据库就存一个session！   
唔，需要的包如下   

    web.py
    - MySQLDb (web.py需要)
    Jinja2
    markdown

####注意模板中index.html和article.html中有几处地方是要复制Disqus的获取评论数或者获取评论的js的，不要忘了   
写作方式就是markdown写作。RSS那里我不是很熟所以貌似写的很烂。   
实际上写的都很烂....QAQ，大牛勿喷...   
膜拜<a href="http://github.com/whtsky">whtsky</a>大神！   
前端后端都是我自己来的..所以貌似整体都很烂..   
啊，sad story   
 
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
    PS:#这里出现错误的时候就是奇葩中文编码的错误，把decode改成gbk试试

###Blog Manager

    eg.blog_bacground_user = 'admin'
       blog_bacground_pass = 'admin'

###MySQL DataBase Structure

    - blog
    -------------
    id         int ,   A_I
    title      text, gb2312_chinese_ci
    time       text, gb2312_chinese_ci
    content    text, gb2312_chinese_ci
    lookcount  int


    - session
    -------------
    session    text, gb2312_chinese_ci


##RP主机配置

* 首先你要git到RP主机上    
* 切换到RicBlog的目录：`cd RicBlog`   
* 编辑好settings.py之后，注意数据库字段啥的要创建好，运行：   
`uwsgi --socket /home/[your-RP-ID]/ricblog.sock --wsgi-file main.py --enable-threads`
/home/[your-RP-ID]/ricblog.sock是自动生成的，不用管。   
然后不要着急查看效果，跑到RP面板配置一下:

- 绑定的域名，就是你的域名
- 数据源：`/home/[your-RP-ID]/web/RicBlog`
- 站点类型是`uWSGI`
- Socket就是上面的你运行的所填写的`/home/[your-RP-ID]/ricblog.sock`
- Alias别名：`/static/ /home/[your-RP-ID]/web/RicBlog/static/`

如果要后台的话，运行如下语句：

    cd RicBlog
    nohup uwsgi --socket /home/[your-RP-ID]/ricblog.sock --wsgi-file main.py --enable-threads &
    exit

以上。   

以上。   
