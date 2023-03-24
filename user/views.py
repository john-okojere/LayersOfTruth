from django.shortcuts import render, redirect
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from .serializers import UserSerializer,  RegisterSerializer
from django.contrib.auth import login, authenticate
from .models import User, OnlineSoul, Prayers, Messages
from .forms import RegisterForm
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django.http import JsonResponse
from django.db.models import Q

from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()

class UserDetailAPI(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


def homepage(request):
    return render(request, 'home/index.html')


def search_memberlist(request, name):
    if name.__len__() > 0:
        members = User.objects.filter(Q(username__icontains=name))
    else:
        members = User.objects.all()
    data = []
    for person in members:
        data.append({
            'id':person.id,
            'username':person.username,
            'first_name':person.first_name,
            'last_name':person.last_name,
            'phone':person.phone,
            'email':person.email,
            'gender':person.gender,
            'role':person.role,
            'date_joined':person.date_joined,
        })
    return JsonResponse(data,safe=False, status=200)
    

def members(request):
    members = User.objects.all()
    return render(request, 'account/members.html',{'members':members})

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            rform = form.save(commit=False)
            rform.role = "USER"
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f"New account created: {username}")
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'account/create.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'account/profile.html')


def createsoul(request):
    name = request.POST.get('soulname')
    phone = request.POST.get('soulphone')

    soul  = OnlineSoul.objects.create(name=name, phone=phone)
    soul.save()
    messages.success(request, 'Your information has been saved, and we will definitely meet you. ')
    return redirect('/')


def createprayer(request):
    name = request.POST.get('soulname2')
    requestp = request.POST.get('soulprayer')

    soul  = Prayers.objects.create(name=name, request=requestp)
    soul.save()
    messages.success(request, 'Your information has been saved, and we will definitely Pray for you. ')
    return redirect('/')


def createmessage(request):
    name = request.POST.get('soulname3')
    email = request.POST.get('soulemail')
    message = request.POST.get('soulmessage')

    soul  = Messages.objects.create(name=name, email=email, message=message)
    soul.save()
    messages.success(request, 'Your information has been saved, and we will definitely get back to you via your email. ')
    return redirect('/')


def soullist(request):
    souls = OnlineSoul.objects.all()
    return render(request, 'account/soul_list.html', {'souls':souls})

def soulprayers(request):
    souls = Prayers.objects.all()
    return render(request, 'account/soul_prayer.html', {'souls':souls})


def soulmessage(request):
    souls = Messages.objects.all()
    return render(request, 'account/soul_message.html', {'souls':souls})

