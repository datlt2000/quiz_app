from django.urls.conf import path
from . import views

app_name = "make_quiz"
urlpatterns = [
    path('', views.MakeQuizView.as_view(), name="create"),
    path('<int:pk>/add-question/', views.AddQuestion.as_view(), name="add_question")
]
