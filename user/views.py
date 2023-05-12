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
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

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
        try: 
            if person.pastor:
                p = 't'
        except:
            p = 'f'
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
            'pastor':p
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

from department.models import Task, Worker
@login_required
def profile(request):
    try:
        worker = Worker.objects.get(user=request.user)
        task = Task.objects.filter(worker = worker )
        return render(request, 'account/profile.html', {'task':task})
    except:
        return render(request, 'account/profile.html')


def createsoul(request):
    name = request.POST.get('soulname')
    phone = request.POST.get('soulphone')

    soul  = OnlineSoul.objects.create(name=name, phone=phone)
    soul.save()
    messages.success(request, 'Your information has been saved, and we will definitely meet you. ')
    return redirect('/')


def createprayer(request):
    first_name = request.POST.get('prayer_first_name')
    last_name = request.POST.get('prayer_last_name')
    email = request.POST.get('prayer_email')
    phone = request.POST.get('prayer_phone')
    requestp = request.POST.get('prayer_request')

    soul  = Prayers.objects.create(first_name=first_name, last_name=last_name,email=email, phone=phone, request=requestp)
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


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'account/password/reset.html'
    email_template_name = 'account/password/reset_email.html'
    subject_template_name = 'account/password/reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login')