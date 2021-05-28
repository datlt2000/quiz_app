from quiz.models import Choice, Question, Quiz
from django.forms.models import inlineformset_factory, modelform_factory
from django.forms import Textarea

QuizForm = modelform_factory(Quiz, fields=["title", "describe"], widgets={"describe": Textarea()})
QuestionForm = modelform_factory(Question, fields=["question_text"])
ChoiceForm = inlineformset_factory(Question, Choice, fields=["choice_text"])