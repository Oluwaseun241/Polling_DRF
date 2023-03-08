from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication

ObtainAuthToken.authentication_classes = [TokenAuthentication]

urlpatterns = [
    # Authentication
    path('auth/', obtain_auth_token),
    path('auth/register', views.register_user),
    path('auth/user', views.user_list),
    
    # Poll
    path('poll/', views.poll_list),
    path('poll/create', views.poll_create),
    path('poll/<int:pk>', views.poll_detail),
    path('poll/<int:pk>/answer', views.create_answer),
]

