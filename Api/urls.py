from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('user/', views.UserList),
    path('poll/', views.PollList),
    path('poll/<int:pk>', views.PollDetail)
    #path('', views.poll_list)
]
