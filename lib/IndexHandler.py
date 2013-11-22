# -*- coding:utf-8 -*-
from BaseHandler import *

class IndexHandler(BaseHandler):
    """
        基于主页的请求，返回数据库中前三篇Blog，传递到模板
    """
    def GET(self):
        articlesList = [article for article in db.select(
            MySQL_blog_table,where = '1',order = 'id desc',limit = 3)]
        for article in articlesList:
            article['content'] = markdown.markdown(article['content'])
        return self.render('index.html', articles = articlesList)

class ArticleAjaxHandler(BaseHandler):
    """
        针对于瀑布流的Ajax请求，返回一篇Blog
    """
    def GET(self):
        id = str(int(web.input().id))
        try:
            article = db.select(
                MySQL_blog_table,
                where = '1',
                order = 'id desc', 
                limit = id + ', 1'
            )[0]
            article['content'] = markdown.markdown(article['content'])
        except:
            return self.render(
                "ajax.html",
                article = {
                    'title': 'None',
                    'content': 'None',
                    'time': 'None',
                    'lookcount': 'None'
                }
            )

        return self.render(
            "ajax.html",
            article = article
        )
