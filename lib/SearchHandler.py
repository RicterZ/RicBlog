# -*- coding:utf-8 -*-
from BaseHandler import *

class SearchHandler(BaseHandler):
    """
        搜索内容
    """
    def GET(self):
        text, articles = web.input().text, []
        articlesList = [article for article in db.select(MySQL_blog_table,where = '1',order = 'id desc')]
        for article in articlesList:
            if text in article['content']:
                article['content'] = markdown.markdown(article['content'])
                articles.append(article)

        return self.render('search.html', articles = articles)
