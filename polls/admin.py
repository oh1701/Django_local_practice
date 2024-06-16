from django.contrib import admin

from polls.models import Question, TestModel

# Register your models here.


class TestModelInline(admin.TabularInline):
    model = TestModel
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [TestModelInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(TestModel)
