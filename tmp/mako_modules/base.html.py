# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1450065290.914
_enable_loop = True
_template_filename = u'E:/ebk\\templates/base.html'
_template_uri = u'base.html'
_source_encoding = 'utf-8'
_exports = ['end', 'right_content']



from constants import PERMISSIONS


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        merchant = context.get('merchant', UNDEFINED)
        self = context.get('self', UNDEFINED)
        user = context.get('user', UNDEFINED)
        static_url = context.get('static_url', UNDEFINED)
        current_user = context.get('current_user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r\n<html xmlns:ng="http://angularjs.org">\r\n    <head>\r\n        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\r\n\r\n        <meta name="renderer" content="webkit"> \r\n        <meta http-equiv="X-UA-Compatible" content="IE=edge" />\r\n\r\n        <title>\u5546\u65c5\u5206\u9500\u7ba1\u7406\u7cfb\u7edf</title>\r\n\r\n        <script>\r\n        if (window.location.host == "ebooking.betterwood.com") {\r\n            var _hmt = _hmt || [];\r\n            (function() {\r\n            var hm = document.createElement("script");\r\n            hm.src = "//hm.baidu.com/hm.js?bdfdf5e780c80fff1d6d3a1f708d0032";\r\n            var s = document.getElementsByTagName("script")[0]; \r\n            s.parentNode.insertBefore(hm, s);\r\n            })();\r\n        } else if (window.location.host == "ebookingtest.betterwood.com") {\r\n\r\n            var _hmt = _hmt || [];\r\n            (function() {\r\n            var hm = document.createElement("script");\r\n            hm.src = "//hm.baidu.com/hm.js?385000e2adcc281fc566e9e409bb69ec";\r\n            var s = document.getElementsByTagName("script")[0]; \r\n            s.parentNode.insertBefore(hm, s);\r\n            })();\r\n\r\n        }\r\n        </script>\r\n\r\n\t\t<script>\r\n\t\t\tvar merchantId = ')
        __M_writer(filters.decode.utf8(user.merchant_id))
        __M_writer(u';\r\n\t\t</script>\r\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(filters.decode.utf8(static_url('css/bootstrap.min.css')))
        __M_writer(u'">\r\n\r\n        <link href="')
        __M_writer(filters.decode.utf8(static_url('css/default.css')))
        __M_writer(u'" rel="stylesheet" type="text/css" >\r\n        <link href="')
        __M_writer(filters.decode.utf8(static_url('css/mod.css')))
        __M_writer(u'" rel="stylesheet" type="text/css" >\r\n\t\t<script src="')
        __M_writer(filters.decode.utf8(static_url('js/angular.js')))
        __M_writer(u'"></script>\r\n        <script src="')
        __M_writer(filters.decode.utf8(static_url('js/md5.js')))
        __M_writer(u'"></script>\r\n\r\n        <script src="')
        __M_writer(filters.decode.utf8(static_url('js/conLogService.js')))
        __M_writer(u'"></script>\r\n        \r\n        <link href="')
        __M_writer(filters.decode.utf8(static_url('image/icon.ico')))
        __M_writer(u'" rel="SHORTCUT ICON">\r\n\r\n\r\n    </head>\r\n    <body>\r\n        <div class="wrapper">\r\n            <!--\u9875\u5934\u90e8\u5206-->   \r\n            <div class="header"><div class="auto">\r\n\r\n                    <!--\u9876\u90e8\u7528\u6237\u4fe1\u606f-->  \r\n                    <div class="admin-info">\r\n                        <div class="fl">\r\n                            <img src="')
        __M_writer(filters.decode.utf8(static_url('image/bg-admin.png')))
        __M_writer(u'" width="80" height="80" class="img3"/>\r\n                            <img src="')
        __M_writer(filters.decode.utf8(static_url('image/admin-head.jpg')))
        __M_writer(u'" class="img-head"/>\r\n                        </div>\r\n                        <div class="fr">\r\n                            \u6b22\u8fce\u56de\u6765\uff01<br/>\r\n\t\t\t\t\t\t\t<strong id="userNameCheck">')
        __M_writer(filters.decode.utf8(user.username))
        __M_writer(u'</strong>\r\n                        </div>\r\n                    </div>\r\n\r\n                    <div class="person-menu">\r\n                        <ul>\r\n')
        if user.username in ['admin', 'root']:
            __M_writer(u'                            <li class="icon-admin"><a href="/userManage/" target="_blank">\u7528\u6237\u7ba1\u7406</a></li>\r\n')
        __M_writer(u'                            <li class="icon-password"><a href="/password/" target="_blank">\u4fee\u6539\u5bc6\u7801</a></li>\r\n                        </ul>\r\n                    </div>\r\n\r\n                    <div class="left">\r\n                        <img src="')
        __M_writer(filters.decode.utf8(static_url('image/logo-sys.png')))
        __M_writer(u'" width="250" height="50" alt="\u65c5\u884c\u793e\u5206\u9500\u7ba1\u7406\u7cfb\u7edf" class="img1"/>\r\n                    </div>\r\n\r\n                    <div class="right">\r\n                        <ul class="right-menu">\r\n                            <li class="icon-out"><a href="javascript:void(0)" id="out-btn">\u9000\u51fa\u7cfb\u7edf</a></li>\r\n                            <li id="qqOnline" class="icon-contact" style="position:relative">\r\n\r\n                                <div  class="qq" id="qqContact">\r\n                                    <div class="borderdis"></div>\r\n                                    <div class="qqcontracter" style="padding-top:10px">\r\n                                        <a target="_blank" href="http://wpa.qq.com/msgrd?v=3&uin=2106806514&site=qq&menu=yes">\r\n                                            <img src="')
        __M_writer(filters.decode.utf8(static_url('image/qq_contact.png')))
        __M_writer(u'">\r\n                                        </a>\r\n                                        <span>\u65c5\u884c\u793e\u5408\u4f5c\u5ba2\u670d  \u6c90\u6c90</span>\r\n                                    </div>\r\n                                    <div class="qqcontracter">\r\n                                        <a target="_blank" href="http://wpa.qq.com/msgrd?v=3&uin=2731202307&site=qq&menu=yes">\r\n                                            <img src="')
        __M_writer(filters.decode.utf8(static_url('image/qq_contact.png')))
        __M_writer(u'">\r\n                                        </a>\r\n                                        <span>\u65c5\u884c\u793e\u5408\u4f5c\u5ba2\u670d cici</span>\r\n                                    </div>\r\n                                    <div class="qqcontracter">\r\n                                        <a target="_blank" href="http://wpa.qq.com/msgrd?v=3&uin=2824471995&site=qq&menu=yes">\r\n                                            <img src="')
        __M_writer(filters.decode.utf8(static_url('image/qq_contact.png')))
        __M_writer(u'">\r\n                                        </a>\r\n                                        <span>\u5355\u4f53\u5408\u4f5c\u9152\u5e97\u5ba2\u670d \u9759\u9759</span>\r\n                                    </div>\r\n                \r\n                                </div> \r\n\r\n                                <a href="#" alt="\u5728\u7ebfQQ\u8054\u7cfb\u6211\u4eec" title="\u5728\u7ebfQQ\u8054\u7cfb\u6211\u4eec">\u5728\u7ebf\u5ba2\u670d</a></li>  \r\n                            <li class="icon-guide"><a href="javascript:void(0)" id="guide-btn">\u65b0\u624b\u5f15\u5bfc</a></li>\r\n                            <li id="qrcode">\r\n                                <a href="javascript:void(0)" id="guide-btn">\u5b98\u65b9\u5fae\u4fe1</a>\r\n                            </li>   \r\n                        </ul>\r\n                    </div>\r\n\r\n            </div></div>\r\n            <!--\u9875\u5934\u90e8\u5206end--> \r\n\r\n             \r\n\r\n\r\n            <!--\u5de6\u4fa7\u90e8\u5206-->  \r\n            <div class="main-left">\r\n\r\n                <!--\u5de6\u4fa7\u83dc\u5355-->   \r\n                <div class="left-menu">\r\n                    <dl class="menu1" style="margin-bottom:0px;">\r\n                        <dt><u class="icon-dt"></u>\u8ba2\u5355\u7ba1\u7406</dt>\r\n                        <dd><a href="/order/waiting/"><u class="icon1"></u>\u5f85\u786e\u8ba4\u8ba2\u5355<b id="orderPoint" class="has-order">\xb7</b></a></dd>\r\n                        <dd><a href="/order/list"><u class="icon2"></u>\u8ba2\u5355\u67e5\u8be2</a></dd>\r\n\r\n                    </dl>\r\n\r\n                    <dl class="menu2" style="margin-bottom:0px;">       \r\n                        <dt><u class="icon-dt"></u>\u5408\u4f5c\u9152\u5e97\u7ba1\u7406</dt>\r\n                        <dd><a href="/hotel/cooped/"><u class="icon4"></u>\u5df2\u5408\u4f5c\u9152\u5e97</a></dd>\r\n')
        if ((current_user.authority & PERMISSIONS.choose_hotel or current_user.type == current_user.TYPE_ADMIN) and (merchant.type == merchant.TYPE_TRAVEL_AGENCY)) or user.type == user.TYPE_ROOT:
            __M_writer(u'                        <dd><a href="/hotel/willcoop/"><u class="icon5"></u>\u53ef\u5408\u4f5c\u9152\u5e97</a></dd>                \r\n')
        __M_writer(u'                    </dl>\r\n\r\n')
        if current_user.type != current_user.TYPE_SUB:
            __M_writer(u'                    <dl class="menu3" style="margin-bottom:0px;">\r\n                        <dt><u class="icon-dt"></u>\u6570\u636e\u7edf\u8ba1</dt>\r\n                        <dd><a href="/static/java/html/orderAnalyse.html?v=20150611"><u class="icon3"></u>\u8ba2\u5355\u7edf\u8ba1</a></dd>\r\n                        <!--<dd><a href="#"><u class="icon3"></u>\u95f4\u591c\u7edf\u8ba1</a></dd>-->\r\n                    </dl>\r\n')
        __M_writer(u'\r\n')
        if current_user.authority & PERMISSIONS.income_statistics or current_user.type == current_user.TYPE_ADMIN or current_user.type == current_user.TYPE_ROOT:
            __M_writer(u'                    <dl class="menu4" style="margin-bottom:0px;">\r\n                        <dt><u class="icon-dt"></u>\u8d22\u52a1\u7edf\u8ba1</dt>\r\n                        <dd><a href="/finance/prepay/"><u class="icon3"></u>\u9884\u4ed8\u7ed3\u7b97</a></dd>\r\n                        <dd><a href="/finance/agency/"><u class="icon3"></u>\u73b0\u4ed8\u7ed3\u7b97</a></dd>\r\n                        <dd><a href="/contract/"><u class="icon3"></u>\u5408\u540c\u7ba1\u7406</a></dd>\r\n                    </dl>\r\n')
        __M_writer(u'\r\n\r\n\r\n                </div>\r\n                <!--\u5de6\u4fa7\u83dc\u5355end-->\r\n            </div>\r\n            <!--\u5de6\u4fa7\u90e8\u5206end--> \r\n\r\n            <!--\u53f3\u4fa7\u90e8\u5206--> \r\n            <div class="main-right">\r\n                ')
        __M_writer(filters.decode.utf8(self.right_content()))
        __M_writer(u'\r\n            </div>\r\n            <!--\u53f3\u4fa7\u90e8\u5206end--> \r\n        </div>\r\n\r\n        <!--\u65b0\u624b\u5f15\u5bfc\u6d6e\u5c42-->     \r\n        <div class="messageDiv" id="guide-div" style=" display:none">\r\n            <div class="messageBlack"></div>\r\n            <div class="detail guide-div">\r\n                <div class="head"><h1>\u65b0\u624b\u5f15\u5bfc</h1></div>\r\n                <p id="closeDiv" class="close" href="#">X</p>\r\n                <div class="con">\r\n                    <p class="f16" style=" text-align:center;padding:30px 0;">\u5982\u679c\u4f60\u662f\u9996\u6b21\u767b\u5f55\u7684\u7528\u6237\uff0c\u8bf7\u6309\u4ee5\u4e0b\u6b65\u9aa4\u64cd\u4f5c\uff1a</p>\r\n                    <p  style=" text-align:center">\r\n\r\n\t\t\t\t\t<img src="')
        __M_writer(filters.decode.utf8(static_url('image/contral-step.jpg')))
        __M_writer(u'" width="331" height="264" />          \r\n                    </p>\r\n                </div>\r\n            </div> \r\n        </div>   \r\n\r\n    </div>   \r\n    <!--\u65b0\u624b\u5f15\u5bfc\u6d6e\u5c42\u7ed3\u675f-->  \r\n\r\n\r\n    <!--\u9000\u51fa\u767b\u5f55\u6d6e\u5c42-->     \r\n    <div class="messageDiv" id="out-div" style=" display:none">\r\n        <div class="messageBlack"></div>\r\n        <div class="detail">\r\n            <div class="head"><h1>\u63d0\u793a</h1></div>       \r\n            <div class="con">\r\n                <p class="f16" style=" text-align:center;padding:30px 0;">\u4f60\u786e\u8ba4\u8981\u9000\u51fa\u5417\uff1f</p>\r\n                <p class="action" style=" text-align:center">\r\n                    <input name="\u786e\u5b9a" type="button" value="\u786e\u5b9a" id="sure-out"/>\r\n                    <input name="\u53d6\u6d88" type="button" value="\u53d6\u6d88" class="btn-bai" id="no-out" />\r\n                </p>\r\n            </div>\r\n        </div> \r\n    </div>   \r\n    <!--\u9000\u51fa\u767b\u5f55\u5f39\u7a97\u6d6e\u5c42\u7ed3\u675f-->  \r\n\t<script src="')
        __M_writer(filters.decode.utf8(static_url('js/jquery1.9.1.js')))
        __M_writer(u'"></script>\r\n\t<script src="')
        __M_writer(filters.decode.utf8(static_url('js/common.js')))
        __M_writer(u'"></script>\r\n\r\n\t')
        __M_writer(filters.decode.utf8(self.end()))
        __M_writer(u'\r\n</body>\r\n</html>\r\n\r\n')
        __M_writer(u'\r\n\r\n')
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_end(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 1, "19": 0, "29": 3, "30": 37, "31": 37, "32": 39, "33": 39, "34": 41, "35": 41, "36": 42, "37": 42, "38": 43, "39": 43, "40": 44, "41": 44, "42": 46, "43": 46, "44": 48, "45": 48, "46": 60, "47": 60, "48": 61, "49": 61, "50": 65, "51": 65, "52": 71, "53": 72, "54": 74, "55": 79, "56": 79, "57": 91, "58": 91, "59": 97, "60": 97, "61": 103, "62": 103, "63": 139, "64": 140, "65": 142, "66": 144, "67": 145, "68": 151, "69": 152, "70": 153, "71": 160, "72": 170, "73": 170, "74": 185, "75": 185, "76": 210, "77": 210, "78": 211, "79": 211, "80": 213, "81": 213, "82": 218, "83": 221, "89": 220, "93": 220, "99": 217, "103": 217, "109": 103}, "uri": "base.html", "filename": "E:/ebk\\templates/base.html"}
__M_END_METADATA
"""
