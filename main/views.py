from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import RegistrationForm
from .models import Announcement, Registration


def index(request):
    return render(request, "index.html", {
        "announcements": Announcement.objects.filter(is_active=True),
        "registrations": Registration.objects.all(),
    })


def register(request):
    form = RegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Готово, вы записаны на теннис! Ваше имя уже в списке.")
        return redirect("index")
    return render(request, "register.html", {"form": form})


def about(request):
    return render(request, "about.html")
