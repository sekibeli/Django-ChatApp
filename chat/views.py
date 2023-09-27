from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Chat, Message
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
 
@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages':  chatMessages})


def login_view(request):
    redirect = request.GET.get('next')
    if request.method == 'POST':
       user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
       if user:
           login(request, user)
           return HttpResponseRedirect(request.POST.get('redirect'))
       else:
           return render(request, 'chat/login.html', {'wrongPassword' : True, 'redirect': redirect})
       
    return render(request,'chat/login.html', {'redirect': redirect})


def signin_view(request):
   # redirect = request.GET.get('next')
    if request.method == 'POST':
        if (request.POST['password'] == request.POST['repeat_password']):
             user = User.objects.create_user(username=request.POST['username'],
                                 email=request.POST['email'],
                                 password=request.POST['password'])
             return render(request, 'chat/login.html')               
        else:
            return render(request,'chat/signin.html', {'wrongRepeatPassword': True }) 
   
    return render(request, 'chat/signin.html' )