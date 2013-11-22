# -*- coding:utf-8 -*-
import os
import web
import time
import random
import markdown
import jinja2 as jj

web.config.debug    = False #!important
templates_path      = 'templates'
MySQL_host          = 'localhost'
MySQL_user          = 'root'
MySQL_pass          = '123456'
MySQL_DB            = 'ricblog'
MySQL_blog_table    = 'blog'
MySQL_user_table    = 'session'

blog_bacground_user = 'admin'
blog_bacground_pass = 'admin'

default_title       = 'Blog'
default_title_des   = ' | RicBlog - 一款轻量级博客'.decode('gbk')
navbar_title        = "RicBlog"
website_keyword     = "网站关键词".decode('gbk')
website_description = 'RicBlog是一款轻量级博客系统'.decode('gbk')

db = web.database(host=MySQL_host, dbn='mysql', db=MySQL_DB, user=MySQL_user, pw=MySQL_pass)
env = jj.Environment(loader = jj.FileSystemLoader(templates_path))
