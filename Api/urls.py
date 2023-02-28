from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('', views.registration_view, name='user_create'),
    path('login/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('poll/', views.PollList),
    path('poll/<int:pk>', views.PollDetail)
    #path('', views.poll_list)
]
