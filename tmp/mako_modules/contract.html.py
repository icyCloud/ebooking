# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1448436196.14
_enable_loop = True
_template_filename = 'E:/ebk\\templates/contract.html'
_template_uri = 'contract.html'
_source_encoding = 'utf-8'
_exports = ['end', 'right_content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_end(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        static_url = context.get('static_url', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n\n    <script src="')
        __M_writer(filters.decode.utf8(static_url('js/contract.js')))
        __M_writer(u'"></script>\n\n    \n   \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n\n<!--\u5bfc\u822a\u6761--> \n\t<div class="notice" id="notice"><h2>\u5408\u540c\u7ba1\u7406</h2></div>\n\t<!--\u5bfc\u822a\u6761end-->  \n\n\t<!--\u4e3b\u4f53\u5185\u5bb9-->  \n\t<div id="ng-app" class="main"\n        ng-app="contractApp"  ng-controller="contractAppCtrl" \n        ><div class="p15">\n       \t\t\n\t\t\t<!--\u5f00\u59cb-->  \n\t\t\t<div class="main-mod main-wcoop">\n\t\t\t\t\n\t\t\t\t<div class="willcoop-div">\n\t\t\t\t\t<div class="content"><div class="p15">\n\n\t\t\t\t\t\t\t<table width="100%" border="0" cellspacing="0" cellpadding="0" class="table-head">\n\t\t\t\t\t\t\t\t<thead><tr>\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t<th width="15%">\u5ba2\u6237\u540d\u79f0</th>\n\t\t\t\t\t\t\t\t\t\t<th width="10%">\u5408\u4f5c\u6a21\u5f0f</th>\n\t\t\t\t\t\t\t\t\t\t<th width="10%">\u4f63\u91d1</th>\n\t\t\t\t\t\t\t\t\t\t<th width="15%">\u5f00\u6237\u540d</th>\n                    \t\t\t\t\t<th width="15%">\u5f00\u6237\u884c</th>\n                    \t\t\t\t\t<th width="27%">\u94f6\u884c\u8d26\u53f7</th>\n')
        if user.username == 'root':
            __M_writer(u'                    \t\t\t\t\t<th width="8%">\u64cd\u4f5c</th>\n')
        __M_writer(u'                    \n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t</tr></thead>\n\t\t\t\t\t\t\t</table> \n\n\n\t\t\t\t\t\t\t<table width="100%" border="0" cellspacing="0" cellpadding="0" class="table01" style="line-height:35px" id="tablerow"\n                               >\n\t\t\t\t\t\t\t\t<tr ng-repeat="contracts in contracts">\n\t\t\t\t\t\t\t\t\t\n                      <td width="15%" ng-bind="contracts.name"></td>\n\n                      <td width="10%" ng-bind="checkType(contracts.type)"></td>\n\n                      <td width="10%" ng-bind="checkCommission(contracts.type,contracts.commission)"></td>\n                      <td width="15%" ng-bind="contracts.bank_account_name"></td>\n                      <td width="15%" ng-bind="contracts.bank_name"></td>\n                      <td width="27%" ng-bind="contracts.bank_account_id"></td>\n')
        if user.username == 'root':
            __M_writer(u'                       <td width="8%"><a ng-click="change($index);" href="#" style="color:#5594D2;text-decoration: underline;">\u4fee\u6539</a></td>\n')
        __M_writer(u'                                    \n\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t</table>\n')
        if user.username == 'root':
            __M_writer(u'\t\t\t\t\t\t\t  <input ng-click="addContractBtn()" type="button" value="+" class="btn-bai" style="margin-top:20px;width:32px;font-size:20px;margin-left:3px;"/>\n')
        __M_writer(u'\n                <p style="margin-top:10px;font-size:10px;margin-left:3px;">\u63d0\u793a\uff1a\u6bcf\u4e2a\u5408\u4f5c\u6a21\u5f0f\u53ea\u6709\u4e00\u4efd\u5408\u540c</p>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t   \n\t\t\t\t\t</div></div>\n\t\t\t\t</div>\n\n\t\t\t</div>\n\t\t\t<!--\u7ed3\u675f-->  \n\n\n        \n\n <!--\u589e\u52a0\u754c\u9762\u5f00\u59cb -->\n\n\t\t\t<div class="messageDiv" ng-show="addcontract" ng-cloak>\n \t\t \t <div class="messageBlack"></div>\n \t\t \t <div class="detail piliang-room" style="width:400px;margin-left:-200px">\n  \t\t    \t<div class="head"><h1>\u589e\u52a0</h1></div>\n    \t\t \t  <div class="con">\n      \t\t \t<table width="100%" border="0" cellspacing="0" cellpadding="0">\n\n            <tr>\n              <td width="125px">\u5ba2\u6237\u540d\u79f0\uff1a</td>\n              <td><input ng-model="addName" class="input-t" type="text"/></td>\n            </tr>\n\n            <tr>\n              <td width="125px">\u5408\u4f5c\u6a21\u5f0f\uff1a</td>\n              <td><select name="" class="input-s"  ng-model="addPayType">\n                       <option value="0">\u73b0\u4ed8</option>\n                       <option value="1">\u9884\u4ed8</option>                      \n                     </select></td>\n            </tr>\n\n            <tr ng-show="moneryShow">\n              <td width="125px">\u4f63\u91d1\uff1a</td>\n              <td><input ng-model="addMonery" class="input-t" type="text"/>&nbsp;%</td>\n            </tr>\n\n            <tr>\n              <td width="125px">\u5f00\u6237\u540d\uff1a</td>\n              <td><input ng-model="addBankName" class="input-t" type="text"/></td>\n            </tr>\n\n  \t\t\t\t\t<tr>\n    \t\t\t\t\t<td width="125px">\u5f00\u6237\u884c\uff1a</td>\n    \t\t\t\t\t<td><input ng-model="addBank" class="input-t" type="text"/></td>\n  \t\t\t\t\t</tr>\n\n  \t\t\t\t\t<tr>\n    \t\t\t\t\t<td >\u94f6\u884c\u8d26\u53f7\uff1a</td>\n    \t\t\t\t\t<td><input ng-model="addCard" class="input-t" type="text"/></td>\n  \t\t\t\t\t</tr>\n\n\t\t\t\t</table>\n\n        <p ng-bind="addContractMsg" style="padding-left:22px;color:red"></p>\n\n\t\t\t\t<p style="text-align:center">\n\t\t\t\t\t<input style="height: 26px;width: 60px;position:relative;top:2px;" name="" type="button" value="\u4fdd\u5b58" ng-click="addCurrentContract()"/> \n\t\t\t\t\t<input name="" type="button" value="\u53d6\u6d88"  ng-click="addCancel()" class="btn-bai btn-s" style="height: 26px;width: 60px;margin-left:20px;" />\n\t\t\t\t</p>\n     \t\t \t </div>\n  \t\t\t </div> \n\t\t\t</div> \n\n\n\n  <!--\u589e\u52a0\u754c\u9762\u7ed3\u675f-->\n\n\n\n <!--\u4fee\u6539\u754c\u9762\u5f00\u59cb -->\n\n      <div class="messageDiv" ng-show="changeContract" ng-cloak>\n       <div class="messageBlack"></div>\n       <div class="detail piliang-room" style="width:400px;margin-left:-200px">\n            <div class="head"><h1>\u4fee\u6539</h1></div>\n            <div class="con">\n            <table width="100%" border="0" cellspacing="0" cellpadding="0">\n\n            <tr>\n              <td width="125px">\u5ba2\u6237\u540d\u79f0\uff1a</td>\n              <td><input ng-model="changeName" class="input-t" type="text"/></td>\n            </tr>\n\n            <tr>\n              <td width="125px">\u5408\u4f5c\u6a21\u5f0f\uff1a</td>\n              <td><select disabled name="" class="input-s"  ng-model="changePayType">\n                       <option value="0">\u73b0\u4ed8</option>\n                       <option value="1">\u9884\u4ed8</option>                      \n                     </select></td>\n            </tr>\n\n            <tr ng-show="!changePayType">\n              <td width="125px">\u4f63\u91d1\uff1a</td>\n              <td><input ng-model="changeMonery" class="input-t" type="text"/>&nbsp;%</td>\n            </tr>\n\n            <tr>\n              <td width="125px">\u5f00\u6237\u540d\uff1a</td>\n              <td><input ng-model="changeBankName" class="input-t" type="text"/></td>\n            </tr>\n\n            <tr>\n              <td width="125px">\u5f00\u6237\u884c\uff1a</td>\n              <td><input ng-model="changeBank" class="input-t" type="text"/></td>\n            </tr>\n\n            <tr>\n              <td >\u94f6\u884c\u8d26\u53f7\uff1a</td>\n              <td><input ng-model="changeCard" class="input-t" type="text"/></td>\n            </tr>\n\n        </table>\n\n        <p ng-bind="changeContractMsg" style="padding-left:22px;color:red"></p>\n\n        <p style="text-align:center">\n          <input style="height: 26px;width: 60px;position:relative;top:2px;" name="" type="button" value="\u4fdd\u5b58" ng-click="changeCurrentContract()"/> \n          <input name="" type="button" value="\u53d6\u6d88" ng-click="changeContract=false;changeContractMsg=\'\'"  class="btn-bai btn-s" style="height: 26px;width: 60px;margin-left:20px;" />\n        </p>\n           </div>\n         </div> \n      </div> \n\n\n\n  <!--\u4fee\u6539\u754c\u9762\u7ed3\u675f-->\n\n\n\n\n\n\t</div></div>\n\t<!--\u4e3b\u4f53\u5185\u5bb9end--> \n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 199, "33": 208, "66": 60, "65": 58, "39": 201, "64": 57, "63": 53, "44": 201, "45": 204, "46": 204, "61": 50, "72": 66, "52": 2, "57": 2, "26": 0, "59": 30, "60": 32, "58": 29, "62": 51, "31": 1}, "uri": "contract.html", "filename": "E:/ebk\\templates/contract.html"}
__M_END_METADATA
"""
