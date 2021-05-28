from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
# Create your views here.


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "user/register.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("home:index")
        return render(request, "user/register.html", {"form": form})
