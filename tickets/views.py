#coding:utf-8
import json

import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

from tickets import biz
from tickets.models import Userinfo


def sign_in(request):
    JSCODE = request.GET.get('code')
    NICKNAME = request.GET.get('nickname')
    APPID = 'wxdc6e33c1ae78a53f'
    SECRET = 'e1b9341980670f6a1a6e44a496b69e9d'
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % (APPID, SECRET, JSCODE)
    resp = requests.get(url=url, verify=False)
    resp = resp.text
    print(resp)
    resp = json.loads(resp)
    # 是否获取code成功，其实有好几种情况为了简便只写了一种
    # if int(resp['errcode']) == 0 or resp.has_key('errcode') == False :  实际上返回结果里没有errcode????
    session_key  = resp['session_key']
    openid = resp['openid']
    # -------  登陆 ----------- 根据openid，判断用户 ----------
    # 把openid 当成password是否可行？从而借用django的登陆？
    # 因为微信nickname不是唯一的，因此，对应关系应该是 openid -- username, openid  -- password,  nickname不用存，即使存了，也不用更新，我们不用关心。
    # 如果全都自己写，会很麻烦很没有效率。

    # 如果没执行过注册，循环登陆、注册。
    # user = authenticate(username=openid, password=openid)
    # if user is not None:
    # # A backend authenticated the credentials
    #     login(request, user)
    #     print("login ")
    #     return HttpResponse('login success')
    # else:
    # # No backend authenticated the credentials
    #     user = User.objects.create_user(username=openid, password=openid, first_name=NICKNAME)
    #     user.last_name = NICKNAME
    #     login(request,user)
    #     print('regist and login')
    #     return  HttpResponse('login success')

    # 管理、生成登陆态
    usermanage = biz.UserManage()
    # 判断是否有注册过
    sid = usermanage.login(openid=openid, session_key=session_key, username=NICKNAME)
    resp = {'sid': sid }
    return HttpResponse(json.dumps(resp,ensure_ascii=False), content_type='application/json')

# @login_required
def create_ticket(request):
    usermanage = biz.UserManage()
    sid = request.META.get('HTTP_SID')
    # 如果有sid
        # Python中对变量是否为None的判断
            # 三种主要的写法有：
            #
            # 第一种：if X is None;
            #
            # 第二种：if not X；
            #
            # 当X为None, False, 空字符串
            # "", 0, 空列表[], 空字典
            # {}, 空元组()
            # 这些时，not X为真，即无法分辨出他们之间的不同。
            #
            # 第三种：if not X is None;
    message = ''
    success = 0
    req = json.loads(request.body)
    print(sid)
    if sid:
        print('00000000000000000000000000')
        print(type(sid))
        print(sid)
        # 检查各个信息是否全
        if not req['type'] or req['type'] == '0':
            print(1)
            message = '选择类型'
        if not req['price']:
            print(2)
            message = '填写价格'
        if not req['renpin']:
            print(3)
            message = '填写人品'
        if not req['addr']:
            print(4)
            message = '填写地址'
        if not message:
            print(5)
            success = 1
    else:
        message = '缺少sid'

    if success == 1:

        print(request.body)
        ticket = {
            'type':req['type'],
            'price':req['price'],
            'renpin':req['renpin'],
            'addr':req['addr'],
            'date':req['date'],
            'sid':sid
        }
        ticketmanage = biz.TicketManage()
        ticketmanage.createTicket(ticket)

    resp = {
        'success':success,
        'message':message
    }
    print(resp)
    return HttpResponse(json.dumps(resp,ensure_ascii=False), content_type='application/json')

def ticket_list(request):
    type = request.GET.get('type')
    resp = {
        'total':15,
        'list':
        [{
        'id':1501,
        'price':150.00,
        'renpin':1500,
        'addr':'南楼18层',
        'time':1548989176000
    },{
        'id': 1502,
        'price':120.00,
        'renpin':1200,
        'addr':'鼎好6层',
        'time':1548987176000
    },{
        'id': 1503,
        'price':100.00,
        'renpin':1000,
        'addr':'鼎好5层',
        'time':1548981176000
    }]}
    return HttpResponse(json.dumps(resp,ensure_ascii=False), content_type='application/json')

# @login_required
def book_ticket(request):
    resp = {
        'isSuccess':True,
        'ticket':{
            'price':120.00,
            'renpin':1200,
            'time':1548987176,
            'name':'尉迟敬德',
            'phone':'18518610123',
            'addr':'鼎好6层',
        }
    }
    return HttpResponse(json.dumps(resp,ensure_ascii=False), content_type='application/json')

def my_info(request):
    resp = {
        'renpin':1000,
        'wanted':10,
        'sent':12,
        'wechat':'helloenola',
        'phone':'18622749772',
        'addr':'鼎好6层',
    }
    return HttpResponse(json.dumps(resp,ensure_ascii=False), content_type='application/json, charset=utf-8')

def mock(request):
    usermanage = biz.UserManage()
    # sid = usermanage.register(openid=452435, session_key=2435, username= 'zxxa')
    # userid = usermanage.findUserID(sid = 'f80f83746e79f9df873d2dcfcb534e3598a424cd')
    userls = usermanage.findUserAll(sid = 'f80f83746e79f9df873d2dcfcb534e3598a424cd')
    print(userls)
    return HttpResponse(userls)