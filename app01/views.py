from django.shortcuts import render,redirect,HttpResponse
from app01 import models

def login(request):

    return render(request,"login.html")

def index(request):
    #     取所有调查问卷名称
    questionnaire_list=models.Questionnaire.objects.all()
    return render(request,"index.html",{"questionnaire_list":questionnaire_list})


def quest(request):
    #     取所有问题
    question_list=models.Question.objects.filter()
    print(question_list)
    return render(request,"quest.html",{"question_list":question_list})