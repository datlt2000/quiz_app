from django.urls.conf import path
from . import views

app_name = "home"
urlpatterns = [
    path('', views.HomeView.as_view(), name="index")
]
