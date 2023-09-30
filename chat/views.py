from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Chat, Message
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
import json



 
@login_required(login_url='/login/')
def index(request):
   
    if request.method == 'POST':
        myChat = Chat.objects.get(id=1)
        lastMessage = Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
        data = serializers.serialize('json', [lastMessage, ])
        dataList = json.loads(data)
        # data = {
        #     'text': lastMessage.text,
        #     'created_at': lastMessage.created_at.strftime('%d.%m.%Y'), 
        #     'author': lastMessage.author.username  
        # }
        dataList[0]['fields']['author'] = lastMessage.author.username
        dataList[0]['fields']['receiver'] = lastMessage.receiver.username
        print(dataList)
        return JsonResponse(dataList, safe=False)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages':  chatMessages})


def login_view(request):
    if request.GET.get('next') != None:
        print(request.GET.get('next'))
        redirect = request.GET.get('next')
    else:
        redirect = '/chat'
      
    if request.method == 'POST':
       user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
       if user:
           login(request, user)
           return HttpResponseRedirect('/chat')
       else:
            return JsonResponse({'status': 'error', 'message': 'Benutzername oder Passwort ist falsch!'}, status=400)
    return render(request,'chat/login.html', {'redirect': redirect})


def signin_view(request):
    if request.method == 'POST':
        if (request.POST['password'] == request.POST['repeat_password']):
             user = User.objects.create_user(username=request.POST['username'],
                                 email=request.POST['email'],
                                 password=request.POST['password'])
             return redirect('login')              
        else:
             return JsonResponse({'status': 'error', 'message': 'Die Passwortfelder stimmen nicht überein!'}, status=400)
           # return render(request,'chat/signin.html', {'wrongRepeatPassword': True }) 
    return render(request, 'chat/signin.html' )


def logout_view(request):
    logout(request)
    return redirect('login')
   # return render(request, 'chat/login.html', {'loggedOut': True})
   
   
def overview_view(request):
    allUsers = User.objects.all()
    return render(request, 'chat/overview.html', {'allUsers': allUsers})