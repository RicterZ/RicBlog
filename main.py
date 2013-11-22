# -*- coding:utf-8 -*-

import web
from urls import *
from setting import *

#application = web.application(urls, globals()).wsgifunc()
#以上语句是uwsgi的运行模式

app = web.application(urls, globals())
if __name__ == "__main__":
    app.run()
