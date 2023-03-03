from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    # Authentication
    path('auth/', obtain_auth_token),
    path('register/', views.RegisterUser),
    path('user/', views.UserList),
    
    # Poll
    path('poll/', views.PollList),
    path('poll/<int:pk>', views.PollDetail),
    path('poll/answer/<int:pk>', views.Answer)
]
