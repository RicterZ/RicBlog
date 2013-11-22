# -*- coding:utf-8 -*-
from BaseHandler import *

class ArticleHandler(BaseHandler):
    """
        文章请求处理，实现两个功能
        --------------------------------
        1.获取文章ID，现实文章单页
        2.POST方式发布文章
        --------------------------------
    """
    def GET(self):
        id = int(web.input().id)
        blogContent = db.select(MySQL_blog_table,where = 'id=' + str(id))[0]
        db.update(
            MySQL_blog_table,
            lookcount = str(blogContent['lookcount'] + 1),
            where = 'id=' + str(id)
        )
        return self.render(
            "article.html",
            blogContent['title'],
            blog_id   = blogContent['id'],
            blog_title   = blogContent['title'],
            blog_content = markdown.markdown(blogContent['content']),
            blog_time    = blogContent['time'],
            blog_click   = blogContent['lookcount']
        )

    def POST(self):
        if self.isLogin:
            title = web.input().article_title
            content = web.input().article_content
            nowtime = time.strftime('%Y-%m-%d %H:%M')
            db.insert(
                 MySQL_blog_table,
                 title = title,
                 time = nowtime,
                 content = content
            )
            return web.seeother('/')
