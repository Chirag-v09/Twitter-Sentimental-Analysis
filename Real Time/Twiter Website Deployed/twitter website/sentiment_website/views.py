from django.shortcuts import render
from django.http import HttpResponse
from sentiment_app.models import Users
# Create your views here.


def home(request):
    template = 'home.html'
    users = Users.objects.all()
    _user = []
    _password = []
    for user in users:
        _user.append(user.user)
        _password.append(user.password)
        print(user.user, user.password)
    print(users)
    number = 10
    length = len(_user)
    context = {'number': number, "Users": _user, "Passwords": _password, 'length': length}
    return render(request, template, context)


def error(request):
    template = "home_error.html"
    users = Users.objects.all()
    _user = []
    _password = []
    for user in users:
        _user.append(user.user)
        _password.append(user.password)
        print(user.user, user.password)
    print(users)
    number = 10
    length = len(_user)
    context = {'number': number, "Users": _user, "Passwords": _password, 'length': length}
    return render(request, template, context)


def register(request):
    template = "register.html"
    context = {}
    return render(request, template, context)


def register_enter(request, ID, Password):
    u = Users()
    u.user = ID
    u.password = Password
    u.save()
    template = "save.html"
    context = {}
    return render(request, template, context)

