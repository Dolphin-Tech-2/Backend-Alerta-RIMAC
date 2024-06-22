from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot, name= 'post_chatbot')
]