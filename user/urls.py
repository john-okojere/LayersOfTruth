from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserDetailAPI, signup, profile, members, search_memberlist, createsoul,createprayer, createmessage, soullist, soulprayers, soulmessage

urlpatterns = [
    path("profile/", profile, name="profile"),
    path("search/<str:name>", search_memberlist, name="search-member"),
    path("members/", members, name="members"),
    path("register/",signup , name="register"),
     path('Login/', LoginView.as_view(template_name="account/form.html"), name="login" ),
    path('Logout/', LogoutView.as_view(), name="logout" ),

    path('add-soul/', createsoul, name="addsoul"),
    path('add-prayer/', createprayer, name="addprayer"),
    path('add-message/', createmessage, name="addmessage"),

    path('soul-contact/', soullist, name="soulist"),
    path('soul-prayer/', soulprayers, name="soulprayer"),
    path('soul-message/', soulmessage, name="soulmessage"),
]
