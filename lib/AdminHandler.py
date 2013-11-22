# -*- coding:utf-8 -*-
import string
from BaseHandler import *

class AdminHandler(BaseHandler):
    """
        后台管理
        --------------------------------
        1.GET方式生成后台管理登陆页面
        2.POST方式登陆
        --------------------------------
    """
    def GET(self):
        if not self.isLogin:
            return self.render("login.html")
        else:
            return self.returnManagePage()

    def POST(self):
        username = web.input().username
        password = web.input().password
        if username.upper() == blog_bacground_user.upper() and password == blog_bacground_pass:
            uid = ''.join(random.sample(string.letters+string.digits, 10))
            web.setcookie('uid', uid)
            db.update(MySQL_user_table, where = '1', session = uid)
            return self.returnManagePage()

    def returnManagePage(self):
        return self.render(
            "manage.html",
            "文章发布与管理".decode('utf-8'),
            articleList = db.select(
                MySQL_blog_table,
                what = 'id, title, time',
                where = '1',
                order = 'id desc',
            )
        )

class ArticleEditHandler(BaseHandler):
    """
        文章编辑处理
    """
    def GET(self):
        id = str(int(web.input().id))
        if self.isLogin:
            articleData = db.select(MySQL_blog_table, where = 'id=' + id)[0]
            return self.render(
                "articleEdit.html",
                articleData = articleData
            )

    def POST(self):
        if self.isLogin:
            id = str(int(web.input().id))
            title = web.input().article_title
            content = web.input().article_content
            nowtime = time.strftime('%Y-%m-%d %H:%M')
            db.update(
                 MySQL_blog_table,
                 where = 'id=' + id,
                 title = title,
                 time = nowtime,
                 content = content
            )
            return web.seeother('/')		

class ArticleDelHandler(BaseHandler):
    """
        文章删除请求处理
        --------------------------------
        依据文章ID删除文章
        --------------------------------
    """
    def GET(self):
        id = str(int(web.input().id))
        if self.isLogin:
            db.delete(MySQL_blog_table,where = 'id=' + id)
            return web.seeother('/admin')
		

	
