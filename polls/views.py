from django.http import HttpResponse, response
from django.shortcuts import render

from polls.models import Question


# Create your views here.


def index(request):
    # return HttpResponse("Hello.world.")

    # Question 데이터 중 pub_date 를 정렬하여 5개 까지만 가져옴
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # , 로 연결하여 Return
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voing on question %s." % question_id)