from datetime import timezone

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from lid.forms import LoginForm, RegisterForm, SendMailForm
from lid.models import UsrSendAnswer


def MainView(request):
    if request.user.is_authenticated:
        return redirect('l_auth:detail')
    if 'rg' in request.POST:
        rForm = RegisterForm(request.POST)
        sForm = SendMailForm(request.POST)
        if rForm.is_valid() and sForm.is_valid():
            f_name = rForm.cleaned_data['f_name']
            l_name = rForm.cleaned_data['l_name']
            eml = rForm.cleaned_data['eml']
            usern = rForm.cleaned_data['usern']
            passw = rForm.cleaned_data['passw']
            cpassw = rForm.cleaned_data['cpassw']
            sansw = sForm.cleaned_data['sansw']
            if User.objects.filter(username=usern).exists():
                return redirect('l_auth:main')
            usr = User.objects.create(is_active=True, first_name=f_name, last_name=l_name, email=eml,
                                      password = passw, username=usern,)
            usr.save()
            send_ok = UsrSendAnswer(usr=usr, answr=sansw)
            send_ok.save()
            return redirect('l_auth:detail')
    rForm = RegisterForm()
    sForm = SendMailForm()
    return render(request, 'main.html', {'rForm':rForm, 'sForm':sForm})

def LoginView(request):
    if request.user.is_authenticated:
        return redirect('l_auth:detail')
    pr = 'Login'
    if 'lg' in request.POST:
        lForm = LoginForm(request.POST)
        if lForm.is_valid():
            u = lForm.cleaned_data['usern']
            p = lForm.cleaned_data['passw']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('l_auth:detail')
    lForm = LoginForm()
    return render(request, 'main.html', {'tpr':pr, 'lForm':lForm})

@login_required
def LogOutView(request):
    logout(request)
    return redirect('l_auth:main')

@login_required
def DetailView(request):
    return render(request, 'detail.html')