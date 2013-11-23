# -*- coding:utf-8 -*-
from BaseHandler import *

class RSSHandler(BaseHandler):
    """
        基于主页的请求，返回数据库中前三篇Blog，传递到模板
    """
    def GET(self):
        web.header('Content-type', "text/xml; charset=utf-8")
        articlesList, articlesDataList = [article for article in db.select(
            MySQL_blog_table, where = '1', order = 'id desc')], []
        for article in articlesList:
            article['content'] = '\n'.join(article['content'].split('\n')[0:6]).replace('<', '&lt;').replace('>', '&gt;')
        return self.render('rss.xml', articles = articlesList, url = website_url,
                nowtime = time.strftime(u"%a, %d %b %Y %H:%M:%S GMT", time.gmtime()), 
                title = default_title, name = rss_author, description = website_description
        ) 
