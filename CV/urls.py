from django.urls import path
from . import views

urlpatterns =[
    path('', views.profile, name='success_url'),
    path('index/', views.index, name='index'),
    path('myresume/', views.myresume, name='myresume'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('contact/', views.Comment, name='contact'),
]