from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tickettype(models.Model):
    name = models.CharField(max_length=50)
    # 增删改时间
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)
    is_deleted = models.SmallIntegerField(verbose_name='1-删除，0-有效', default=0)

class Userinfo(models.Model):
    name = models.CharField(max_length=50, blank=True)
    wechat = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    renpin = models.BigIntegerField(verbose_name='人品值', default=0)
    openid = models.CharField(max_length=200, unique=True)
    sid = models.CharField(max_length=200,default='')
    session_key = models.CharField(max_length=200, default='')
    # 增删改时间
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)
    is_deleted = models.SmallIntegerField(verbose_name='1-删除，0-有效', default=0)

class Ticket(models.Model):
    type = models.ForeignKey(Tickettype, verbose_name='发票类型', on_delete=models.CASCADE)
    creator = models.ForeignKey(Userinfo, verbose_name='发布人', on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    renpin = models.BigIntegerField()
    status = models.SmallIntegerField(verbose_name='1-待发布，2-发布，3-成交，4-退款')
    # 增删改时间
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.SmallIntegerField(verbose_name='1-删除，0-有效', default=0)