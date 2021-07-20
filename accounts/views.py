from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib import messages
from django.core.mail import send_mail
import random


def login(request):
    if request.session.has_key('uid'):
        context = {'username': request.session['uid']}
        return render(request, 'accounts/services.html', context)
    if request.method == 'POST':
        curr_user = Accounts.objects.all().filter(
            pk=request.POST["username"], password=request.POST["password"])
        if curr_user.count() == 1:
            request.session['uid'] = request.POST["username"]
            context = {'username': request.session['uid']}
            return render(request, 'accounts/services.html', context)
        else:
            messages.info(request, "Invalid User or Password")
    context = {}
    return render(request, 'accounts/login.html', context)


def register(request):
    if request.session.has_key('uid'):
        del request.session['uid']
    if request.method == 'POST':
        if request.POST["pass1"] == request.POST["pass2"]:
            account_form = Accounts()
            account_form.user_name = request.POST["username"]
            account_form.email = request.POST["email"]
            account_form.phone_num = request.POST["phone_num"]
            account_form.password = request.POST["pass1"]
            account_form.save()
            return render(request, 'accounts/login.html')
        else:
            return HttpResponse("password dosen't match")

    context = {}
    return render(request, 'accounts/register.html', context)


def forgotPassword(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'accounts/forgotPassword.html', context)
    else:
        email = request.POST['email']
        if Accounts.objects.filter(email=email):
            pswrd = Accounts.objects.get(email=email).password

            send_mail('Your Account Password ', 'Your account password at LNMshop Is:' + str(pswrd),
                      'yourpersonalbot@gmail.com', [email])
            error = "Password sent to your Email. Check Inbox"
            return render(request, 'accounts/forgotPassword.html', {'error': error})
        else:
            error = " Email Does Not Exist. Please Register"
            return render(request, 'accounts/forgotPassword.html', {'error': error})


def logout(request):
    if request.session.has_key('uid'):
        del request.session['uid']
    return redirect('login')


def contact(request):
    if request.method == 'GET':
        context = {'username': request.session['uid']}
        return render(request, 'accounts/contact.html', context)
    else:
        emailId = request.POST['email']
        name = request.POST['fname']
        content = request.POST['content']
        error = 'Thanks For Contacting Us We Will reach you Soon! :)'
        send_mail('Somebody Contacted Us', str(name) + 'tried to Contact us via email id :' + str(emailId) + '\n' + 'His comments: ' + str(content),
                  'yourpersonalbot@gmail.com', ['yourpersonalbot@gmail.com'])
        return render(request, 'accounts/contact.html', {'error': error})


def profile(request):

    if request.method == 'POST':
        account = Accounts.objects.get(user_name=request.session['uid'])
        account_form = Accountforms(request.POST, instance=account)
        if account_form.is_valid():
            account_form.save()

    account = Accounts.objects.filter(user_name=request.session['uid'])
    context = {'account': account[0], 'username': request.session['uid']}
    return render(request, 'accounts/profile.html', context)


def about(request):
    context = {'username': request.session['uid']}
    return render(request, 'accounts/about.html', context)
