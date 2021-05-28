from django.urls.conf import path
from . import views

app_name = "quiz"
urlpatterns = [
    path('<int:pk>/', views.QuizView.as_view(), name="detail"),
    path('get-question/', views.QuestionView.as_view(), name="get-question")
]
