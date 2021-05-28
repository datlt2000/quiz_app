from django.shortcuts import render
from django.views import generic
from quiz.models import Quiz
# Create your views here.
class HomeView(generic.ListView):
    model = Quiz
    template_name = 'home/home.html'
