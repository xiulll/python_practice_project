from django.db import models

# Create your models here.

class BookInfo(models.Model):
    #id
    name = models.CharField(max_length=20)
    def __str__(self):
        """将模型类以字符串的方式输出"""
        return self.name

# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    def __str__(self):
        return "姓名："+self.name+" 性别："+str(self.gender)
