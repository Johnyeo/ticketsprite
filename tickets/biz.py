# coding:utf-8
import hashlib
import os

from tickets.models import *

sid_openid = {

}


class UserManage(object):
    # 判断是否已经注册
    def is_registed(self, openid):
        return False

    # 是否登陆
    def is_login(self, openid):
        return False

    # 是否注册
    def register(self, openid, session_key, username):
        # 在表里创建用户
        sid = hashlib.sha1(os.urandom(24)).hexdigest()
        user = Userinfo(name=username, openid=openid, sid=sid, session_key=session_key)
        user.save()
        return sid

    # 登陆生成sid
    def login(self, openid, session_key, username):
        try:
            sid = Userinfo.objects.get(openid=openid).sid
            # sid是临时的， 保存在一个dict里
            return sid
        except Userinfo.DoesNotExist as e:
            print(e)
            sid = self.register(openid=openid, session_key=session_key, username=username)
            return sid

    # 通过sid找到用户
    def findUserID(self, sid):
        return Userinfo.objects.get(sid=sid).id

    def findUserOpenid(self, sid):
        return Userinfo.objects.get(sid=sid).openid

    def findUserInfo(self, sid):
        userinfo = {
            'id': '',
            'name': '',
            'wechat': '',
            'phone': '',
            'address': '',
            'renpin': ''
        }
        id = Userinfo.objects.get(sid=sid).id
        name = Userinfo.objects.get(sid=sid).name
        wechat = Userinfo.objects.get(sid=sid).wechat
        phone = Userinfo.objects.get(sid=sid).phone
        address = Userinfo.objects.get(sid=sid).address
        return userinfo

    def findUserRenpin(self, sid):
        return Userinfo.objects.get(sid=sid).renpin

class TicketManage(object):
    def createTicket(self, ticket):
        print(ticket)
        userid = Userinfo.objects.get(sid=ticket['sid'])
        tickettype = Tickettype.objects.get(id=ticket['type'])
        ticketss = Ticket(
            type=tickettype,
            price=ticket['price'],
            renpin=ticket['renpin'],
            address= ticket['addr'],
            date= ticket['date'],
            creator=userid,
            status=1, # 1 新建
            is_delete=0
        )
        ticketss.save()