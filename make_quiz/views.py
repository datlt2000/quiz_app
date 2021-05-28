from django.http.response import HttpResponse
from quiz.models import Question, Quiz
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from .forms import ChoiceForm, QuizForm, QuestionForm
# Create your views here.


class MakeQuizView(LoginRequiredMixin, View):
    def get(self, request):
        form = QuizForm()
        return render(request, "make_quiz/create_quiz.html", {"form": form})

    def post(self, request):
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.user_id = request.user.id
            quiz.save()
            return redirect("make_quiz:add_question", pk=quiz.id)
        return redirect(request.path)


class AddQuestion(LoginRequiredMixin, View):

    def get(self, request, pk):
        quiz = get_object_or_404(Quiz, pk=pk)
        question_form = QuestionForm()
        choice_form = ChoiceForm()
        return render(request, "make_quiz/add_question.html", {"question_form": question_form, "choice_form": choice_form, "quiz": quiz})

    def post(self, request, pk):
        question_form = QuestionForm(request.POST)
        choice_form = ChoiceForm(request.POST)
        if question_form.is_valid() and choice_form.is_valid():
            question = question_form.save(commit=False)
            question.quiz_id = pk
            question.save()
            
            # save choice
            choices = choice_form.save(commit=False)
            for choice in choices:
                choice.question_id = question.id
                choice.save()
        return redirect(request.path)

