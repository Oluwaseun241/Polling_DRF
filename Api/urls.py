from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    # Authentication
    path('auth/', obtain_auth_token),
    path('auth/register/', views.register_user),
    path('auth/user/', views.user_list),
    
    # Poll
    path('poll/', views.poll_list),
    path('poll/<int:pk>', views.poll_detail),
    path('poll/<int:pk>/answer', views.answer)
]
