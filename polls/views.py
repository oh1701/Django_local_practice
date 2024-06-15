from django.http import HttpResponse, response
from django.shortcuts import render, get_object_or_404
from django.template import loader

from polls.models import Question


# Create your views here.


def index(request):
    # return HttpResponse("Hello.world.")

    # Question 데이터 중 pub_date 를 정렬하여 5개 까지만 가져옴
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voing on question %s." % question_id)
