from django.urls.conf import path
from . import views

app_name = "user"
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register")
]
