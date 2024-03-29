from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'), 
    path('chatbot', views.chatbot, name='chatbot'),  
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('chat-history', views.chat_history, name='chat_history'),
]