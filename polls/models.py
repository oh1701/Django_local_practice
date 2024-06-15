from django.db import models


class Question(models.Model):
    def __str__(self):
            return self.question_text

    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)


class TestModel(models.Model):
    def __str__(self):
        return f"{self.question}"

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
