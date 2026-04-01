from django.shortcuts import render
from apps.accounts.models import User


def home(request):
    user = User.objects.filter(is_deleted=False)
    return render(request, "home.html")
