from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Chat, Message, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
import json
from django.db.models import Q



def get_profile_information(receiver_id):
    """
    Retrieves the profile information of a user based on the provided receiver ID.
    
    Args:
        receiver_id (int): The ID of the receiver whose profile information is to be fetched.
    
    Returns:
        tuple: A tuple containing the receiver object and their associated base64 encoded profile image.
    """
    receiver = User.objects.get(id=receiver_id)
    user_profile = UserProfile.objects.get(user=receiver)
    base64_image = user_profile.base64_image
    return receiver, base64_image


def handle_post_request(request):
    """
    Handles a POST request to create and return a new chat message.
    
    Args:
        request (HttpRequest): The incoming HTTP POST request.
        
    Returns:
        JsonResponse: A JSON response containing the serialized chat message if created.
        None: If the required parameters are not found in the request.
    """
    myChat = Chat.objects.get(id=1)
    receiver_id = int(request.POST.get('receiver_id'))
    textmessage = request.POST.get('textmessage')
    
    if receiver_id and textmessage:
        receiver = User.objects.get(id=receiver_id)
        lastMessage = Message.objects.create(text=textmessage, chat=myChat, author=request.user, receiver=receiver)
        
        data = serializers.serialize('json', [lastMessage,])
        dataList = json.loads(data)
        dataList[0]['fields']['author'] = lastMessage.author.username
        dataList[0]['fields']['receiver'] = lastMessage.receiver.username
        return JsonResponse(dataList, safe=False)
    return None


def get_chat_messages(request, receiver_id):
    """
    Fetches chat messages exchanged between the authenticated user and the specified receiver.
    
    Args:
        request (HttpRequest): The incoming HTTP request.
        receiver_id (int): The ID of the receiver with whom chat messages are to be fetched.
    
    Returns:
        QuerySet: A QuerySet containing chat messages sorted by creation date and time.
    """
    return Message.objects.filter(
        Q(author_id=request.user) & Q(receiver_id=receiver_id) |
        Q(author_id=receiver_id) & Q(receiver_id=request.user)
    ).order_by('created_at', 'time_created')

@login_required(login_url='/login/')
def index(request):
    """
    Main chat view handler that displays chat messages and facilitates message creation.
    
    For GET requests:
        Displays chat messages between the authenticated user and the specified receiver.
        
    For POST requests:
        Handles the creation of a new chat message and returns a JSON response.
    
    Args:
        request (HttpRequest): The incoming HTTP request.
    
    Returns:
        HttpResponse: Rendered HTML response for the chat view.
    """
    base64_image = None
    receiver = None

    receiver_id = request.GET.get('receiver_id')
    if receiver_id:
        receiver, base64_image = get_profile_information(receiver_id)
  
    if request.method == 'POST':
        response = handle_post_request(request)
        if response:
            return response

    chatMessages = get_chat_messages(request, receiver_id)

    return render(request, 'chat/index.html', {'messages': chatMessages, 'receiver': receiver, 'img': base64_image})


def login_view(request):
    """
    Handles user authentication and login.

    For GET requests:
    - Displays the login form. If a 'next' parameter is present in the URL, it determines the redirection path after a successful login. Defaults to '/chat' if 'next' is absent.

    For POST requests:
    - Authenticates the user using provided username and password.
    - If authentication succeeds, logs the user in and redirects to the chat view or the URL specified by the 'next' parameter.
    - If authentication fails, returns a JSON error response.

    Renders the login template for GET requests or unauthenticated POST requests.
    """
    if request.GET.get('next') != None:
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
    """
    Handles user registration.

    For POST requests:
    - Validates if the password and its repeated value match.
    - If they match, creates a new user with the provided username, email, and password, then redirects to the login view.
    - If they don't match, returns a JSON error response indicating the mismatch.

    For GET requests:
    - Displays the registration form.

    Renders the registration template.
    """
    if request.method == 'POST':
        if (request.POST['password'] == request.POST['repeat_password']):
             user = User.objects.create_user(username=request.POST['username'],
                                 email=request.POST['email'],
                                 password=request.POST['password'])
             return redirect('login')              
        else:
             return JsonResponse({'status': 'error', 'message': 'Die Passwortfelder stimmen nicht überein!'}, status=400)
    return render(request, 'chat/signin.html' )


def logout_view(request):
    """
    Logs out the currently authenticated user and redirects them to the login view.
    """
    logout(request)
    return redirect('login')
     
   
def overview_view(request):
    """
    Retrieves and displays a list of all registered users in the system. 
    Renders the overview template for user presentation.
    """
   # allUsers = User.objects.all()
    #return render(request, 'chat/overview.html', {'allUsers': allUsers})
    users_with_profiles = User.objects.select_related('userprofile').all()
    return render(request, 'chat/overview.html', {'users_with_profiles': users_with_profiles})