from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

from .models import Eventos
from .serializers import EventosSerializer

import random

@api_view(['GET'])
def get_eventos(request):
    # Mostrar solo los 10 primeros.
    eventos = Eventos.objects.all()
    serializer = EventosSerializer(eventos, many= True)
    
    return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(['GET'])
def get_eventos_by_state(request):
    # Que solo filtre los que dicen ATENDIENDO.
    eventos = Eventos.objects.filter(estado= 'ATENDIENDO')
    serializer = EventosSerializer(eventos, many= True)
    
    return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(['GET'])
def get_evento(request, id):
    # Que solo filtre un evento por id.
    evento = Eventos.objects.get(id= id)
    serializer = EventosSerializer(evento)
    return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(['GET'])
def get_evento_random(request):
    # Obtener la cantidad de filas en la tabla.
    cantidad = Eventos.objects.count()

    # Que solo filtre un evento por id.
    evento = Eventos.objects.get(id= random.randint(1, cantidad))
    serializer = EventosSerializer(evento)
    
    return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(['POST'])
def post_eventos(request):
    data = request.data
    serializer = EventosSerializer(data= data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


