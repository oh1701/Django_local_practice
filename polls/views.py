from django.http import HttpResponse, response, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic

from polls.models import Question, TestModel


# Create your views here.


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_object(self, queryset=None):
        question_id = self.kwargs.get("question_id")
        return get_object_or_404(Question, id=question_id)


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_object(self, queryset=None):
        question_id = self.kwargs.get("question_id")
        return get_object_or_404(Question, id=question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.testmodel_set.get(pk=request.POST['choice'])
    except (KeyError, TestModel.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
