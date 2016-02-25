from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm

# Create your views here.
def register(request):
    abc = 'abc'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            abc = request.POST['username']
            abc = request.POST['password']
            abc = request.POST['email']
            return HttpResponse(abc)
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'abc':abc, 'form':form})


def login(request):
    return render(request, 'account/login.html')