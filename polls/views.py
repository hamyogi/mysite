from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Question
from polls.models import Choice


def index(request):
    list = Question.objects.all()
    return render(request, 'polls/index.html', {'question': list})


def detail(request, id):

    question = Question.objects.get(pk=id)
    return render(request, 'polls/detail.html', {'item': question})


def vote(request):
    choice = request.POST['choice']
    c = Choice.objects.get(pk=choice)
    c.votes += 1
    c.save()
    print('@@@@@@@@@', choice)
    return render(request, 'polls/vote.html', {'result': c})


def data(email, number):
    # value = request.GET['user_name']
    return HttpResponse(value + email + str(number))


from django.utils import timezone


def add_question(request):
    # text = request.post['text']
    # q = Question(question_text=text, pub_date=timezone.now())
    # q.save()
    # return render(request, 'polls/detail.html', {})
    return HttpResponse('입력완료')


def input(request):
    return render(request, 'polls/input.html', {})


def result(request, id):
    question = Question.objects.get(pk=id)

    return render(request, 'polls/result.html', {'q': question})