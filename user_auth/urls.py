from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='userlogin'),
    path('logout/',views.userLogout, name='userlogout'),
    path('editprofile/', views.UpdateUserView.as_view(), name='editprofile'),
    path('register/', views.RegisterView.as_view(), name='register'),
]

