from django.shortcuts import render

from pools.models import Question, Choice


def index(request):
    Question.objects.order_by('-pub_date')
    questions = Question.objects.all()
    return render(request,'index.html', {'questions' : questions})

def question(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = question.choices.all()
    return render(request, 'question.html',
                  {'question': question, 'choices': choices})

