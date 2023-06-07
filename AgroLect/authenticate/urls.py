from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login1, name='login'),
    path('signup/',views.signup,name='signup'),
    path('signout/', views.signout, name='signout'),
]
