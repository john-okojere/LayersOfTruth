from django.urls import path
from .views import verify_card, Attendance_scanner,food_verify_card, Food_scanner, transport_verify_card,Transport_scanner, Signout_scanner, signout_card, accommodation_card, Accommodation_scanner

urlpatterns = [
    path('Attendance/<int:pk>',Attendance_scanner , name="scanner"),
    path('card/<int:list>/<uuid:uid>', verify_card, name="verify_card"),
 
    path('Food/<int:pk>',Food_scanner , name="food_scanner"),
    path('Food-card/<int:list>/<uuid:pk>', food_verify_card, name="food_verify_card"),
 
    path('transport/<int:pk>',Transport_scanner , name="transport_scanner"),
    path('transport-card/<int:list>/<uuid:pk>', transport_verify_card, name="transport_verify_card"),

    path('accomodation/<int:pk>',Accommodation_scanner , name="accomodation_scanner"),
    path('accomodation-card/<int:list>/<uuid:pk>', accommodation_card, name="accomodation_verify_card"),

    
    path('sign-out/<int:pk>',Signout_scanner , name="signout_scanner"),
    path('signout-card/<int:list>/<uuid:pk>', signout_card, name="signout_verify_card"),

]

