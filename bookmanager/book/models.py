from django.db import models

# Create your models here.

class BookInfo(models.Model):
    #id
    name = models.CharField(max_length=20)

# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
