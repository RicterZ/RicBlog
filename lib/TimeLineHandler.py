# -*- coding:utf-8 -*-
from BaseHandler import *

class TimeLineHandler(BaseHandler):
    def GET(self):
        articlesList = [article for article in db.select(
            MySQL_blog_table,where = '1',order = 'id desc')]
        return self.render('timeline.html', articles = articlesList)
