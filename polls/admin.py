from django.contrib import admin

from polls.models import Question, TestModel

# Register your models here.

admin.site.register(Question)
admin.site.register(TestModel)
