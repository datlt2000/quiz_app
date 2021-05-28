from django.http.response import JsonResponse
from django.views.generic import DetailView
from django.views.generic.base import View
from .models import Question
from .models import Quiz
from .models import Choice

# Create your views here.
class QuizView(DetailView):
    model = Quiz
    template_name = 'quiz/quiz.html'

class QuestionView(View):
    def get(self, request):
        pk = request.GET["quiz"]
        question = list(Question.objects.filter(quiz_id=pk).values())
        for i in range(len(question)):
            question[i]["choice"] = list(Choice.objects.filter(question_id=question[i]["id"]).values())
        return JsonResponse({'data': question}, safe=False)