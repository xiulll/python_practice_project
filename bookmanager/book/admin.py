from django.contrib import admin
from book.models import BookInfo,PeopleInfo

# Register your models here.

#注册书籍类型
admin.site.register(BookInfo)
#注册任务模型
admin.site.register(PeopleInfo)

