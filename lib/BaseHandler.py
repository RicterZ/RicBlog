# -*- coding:utf-8 -*-
from setting import *

class BaseHandler:
    """
        每个请求处理类的基类
    """
    isLogin = False

    def __init__(self):
        """
            初始化
        """
        web.header('Content-type', "text/html; charset=utf-8")
        try: 
            uid = web.cookies().uid
        except:
            self.isLogin = False
            uid = 0
        server_uid = db.select(MySQL_user_table)[0]['session']
        if uid == server_uid:
            self.isLogin = True

    def render(self, templatefile, title = default_title, **kwargs):
        """
            部署到模板
        """
        return env.get_template(templatefile).render(
             navbar_title = navbar_title,
             website_description = website_description,
             website_keyword = website_keyword,
             title = title + default_title_des,
             **kwargs
        )
