# coding:utf-8

from django.db import models

  0.arField(max_length = 64)

class express_message(models.Model):
    user_ID = models.CharField(max_length=18)
    order_ID = models.CharField(max_length=32,null=True)
    send_time = models.DateTimeField(null=True)
    security_check_time = models.DateTimeField(null=True)
    save_time = models.DateTimeField(null=True)
