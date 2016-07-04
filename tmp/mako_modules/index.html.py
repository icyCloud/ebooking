# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1448361604.113
_enable_loop = True
_template_filename = 'E:/ebk\\templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        static_url = context.get('static_url', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r\n<html xmlns:ng="http://angularjs.org">\r\n<head>\r\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\r\n\r\n<meta name="renderer" content="webkit"> \r\n<meta http-equiv="X-UA-Compatible" content="IE=edge" />\r\n\r\n<title>\u5546\u65c5\u5206\u9500\u7ba1\u7406\u7cfb\u7edf</title>\r\n\r\n\r\n<link href="')
        __M_writer(filters.decode.utf8( static_url('css/front.css')))
        __M_writer(u'" rel="stylesheet" type="text/css" >\r\n<script src="')
        __M_writer(filters.decode.utf8(static_url('js/angular.js')))
        __M_writer(u'"></script>\r\n  <script src="')
        __M_writer(filters.decode.utf8(static_url('js/md5.js')))
        __M_writer(u'"></script>\r\n\r\n  <link href="')
        __M_writer(filters.decode.utf8(static_url('image/icon.ico')))
        __M_writer(u'" rel="SHORTCUT ICON">\r\n\r\n</head>\r\n<body>\r\n\r\n<div class="wrapper login">\r\n\r\n <!--\u9875\u5934-->  \r\n    <div class="header"><div class="w1200">\r\n       <div class="left">\r\n\t\t   <a href="#"><img src="')
        __M_writer(filters.decode.utf8(static_url('image/logo.png')))
        __M_writer(u'" width="250" height="50" alt="\u4f18\u54c1\u623f\u6e90" class="img1"/>\r\n\t\t   <img src="')
        __M_writer(filters.decode.utf8(static_url('image/logo-front.png')))
        __M_writer(u'" width="260" height="50" alt="\u65c5\u884c\u793e\u5206\u9500\u7ba1\u7406\u7cfb\u7edf" class="img2"/></a>\r\n       </div>\r\n       \r\n       <div class="right">\r\n          <ul class="right-menu">\r\n          <li class="icon-contact"><a alt="\u5728\u7ebfQQ\u8054\u7cfb\u6211\u4eec" title="\u5728\u7ebfQQ\u8054\u7cfb\u6211\u4eec" target="_blank" href="http://wpa.qq.com/msgrd?v=3&uin=1816777547&site=qq&menu=yes">\u5728\u7ebf\u5ba2\u670d</a></li>          \r\n          <li class="icon-mima"><a alt="\u8054\u7cfb\u5728\u7ebf\u5ba2\u670d\u627e\u56de\u5bc6\u7801" title="\u8054\u7cfb\u5728\u7ebf\u5ba2\u670d\u627e\u56de\u5bc6\u7801" target="_blank" href="http://wpa.qq.com/msgrd?v=3&uin=1816777547&site=qq&menu=yes">\u627e\u56de\u5bc6\u7801</a></li>    \r\n          <li class="icon-addus"><a alt="\u8054\u7cfb\u5728\u7ebf\u5ba2\u670d\u7533\u8bf7\u52a0\u76df" title="\u8054\u7cfb\u5728\u7ebf\u5ba2\u670d\u7533\u8bf7\u52a0\u76df" target="_blank" href="http://wpa.qq.com/msgrd?v=3&uin=1816777547&site=qq&menu=yes">\u7533\u8bf7\u52a0\u76df</a></li>      \r\n          </ul>\r\n       </div>\r\n       \r\n  </div></div>\r\n  <!--\u9875\u5934end--> \r\n  \r\n   \r\n    <!--\u4e2d\u95f4-->   \r\n    <div id="ng-app"  class="main"\r\n\t\tng-app="LoginApp"\r\n\t\tng-controller="LoginCtrl"\r\n\t\t>\r\n        <div class="index-focus">\r\n        \r\n             <div class="mod-login">\r\n             <div class="c1"></div><!--\u900f\u660e\u5c42--> \r\n             <div class="c2">\r\n               <div class="head"><strong>\u767b \u5f55</strong></div>\r\n                 \r\n               <div class="login-label">\r\n                     <label><u class="icon-user01"></u>\r\n                     <input name="user-mumber" type="text" placeholder="\u5ba2\u6237\u7f16\u53f7" maxlength="20"\r\n\t\t\t\t\t\tng-model="merchantId"\r\n\t\t\t\t\t /></label>\r\n                     \r\n                   <label><u class="icon-user02"></u>\r\n                   <input name="user-name" type="text" placeholder="\u7528\u6237\u540d" maxlength="20"\r\n\t\t\t\t\tng-model="username"\r\n\t\t\t\t   /></label>\r\n                   \r\n                     <label><u class="icon-user03"></u>\r\n                     <input name="user-password" type="password" placeholder="\u5bc6\u7801"\r\n\t\t\t\t\t\tng-model="password"\r\n\t\t\t\t\t /></label>\r\n                     \r\n               \r\n                     \r\n\t\t\t\t <label class="input01"><p class="red-tips" ng-bind="errMsg"></p></label>\r\n                 <label class="input02"><input name="" type="button" value="\u767b \u5f55" class="btn-login" ng-click="login()" /></label>\r\n                  \r\n                 </div>\r\n            </div></div>\r\n        </div>\r\n    </div>\r\n    <!--\u4e2d\u95f4end--> \r\n    \r\n     <!--\u9875\u811a-->  \r\n    <div class="footer">\r\n       <div class="w1200">\r\n          <p>\u4e1a\u52a1\u6d3d\u8c08\uff1a400-610-8300&nbsp;&nbsp;&nbsp;&nbsp;\u5ba2\u670d\u70ed\u7ebf\uff1a400-610-8300</p>\r\n          \xa9 1999 - 2015 betterwood. All Rights Reserved. &nbsp; \u7ca4ICP\u590712047659\u53f7</p>\r\n       </div>\r\n    </div>\r\n    <!--\u9875\u811aend-->\r\n    <script src="')
        __M_writer(filters.decode.utf8(static_url('js/jquery-1.8.3.min.js')))
        __M_writer(u'"></script>\r\n\t<script src="')
        __M_writer(filters.decode.utf8(static_url('js/login.js')))
        __M_writer(u'"></script>\r\n</div>\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 27, "33": 27, "34": 89, "35": 89, "36": 90, "37": 90, "43": 37, "15": 0, "21": 1, "22": 12, "23": 12, "24": 13, "25": 13, "26": 14, "27": 14, "28": 16, "29": 16, "30": 26, "31": 26}, "uri": "index.html", "filename": "E:/ebk\\templates/index.html"}
__M_END_METADATA
"""
