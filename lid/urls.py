from django.urls import path, include

from lid import views


app_name='l_auth'
urlpatterns = [
    path('', include('social_django.urls')),
    path('', views.MainView, name='main'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogOutView, name='logout'),
    path('detail/', views.DetailView, name='detail'),
]