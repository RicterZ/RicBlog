from lib.BaseHandler import *
from lib.IndexHandler import *
from lib.AdminHandler import *
from lib.ArticleHandler import *
from lib.SearchHandler import *
from lib.TimeLineHandler import *

urls=(
    '/'             , 'IndexHandler'      ,
    '/search'       , 'SearchHandler'     ,
    '/article_ajax' , 'ArticleAjaxHandler',
    '/article_del'  , 'ArticleDelHandler' ,
    '/article_edit' , 'ArticleEditHandler',
    '/article'      , 'ArticleHandler'    ,
    '/admin'        , 'AdminHandler'      ,
    '/timeline'     , 'TimeLineHandler'
)
