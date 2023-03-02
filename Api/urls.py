from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserList),
    path('register/', views.RegisterUser),
    path('poll/', views.PollList),
    path('poll/<int:pk>', views.PollDetail)
    #path('', views.poll_list)
]
