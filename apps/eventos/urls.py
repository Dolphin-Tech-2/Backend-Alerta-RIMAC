from django.urls import path
from . import views

urlpatterns = [
    path('get_eventos/', views.get_eventos, name= 'get_eventos'),
    path('post_eventos/', views.post_eventos, name= 'post_eventos'),
    path('get_eventos_by_state/', views.get_eventos_by_state, name= 'get_eventos_by_state'),
    path('get_evento/<int:id>/', views.get_evento, name= 'get_evento'),
    path('get_evento_random/', views.get_evento_random, name= 'get_evento_random')
]