from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

from .models import ChatBot
from .serializers import ChatBotSerializer

import google.generativeai as genai

# Create a generative model.
genai.configure(api_key= 'AIzaSyD-QCHV_3TeGPknu_S2-SnjBfrIIUA5tfg')
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

# Create your views here.
@api_view(['POST'])
def chatbot(request):
    data = request.data
    text = data['text_input'].strip()

    if not text:
        return Response({'error': 'Por favor introduce un texto'}, status= status.HTTP_400_BAD_REQUEST)

    response = chat.send_message(text)
    
    chatbot = ChatBot.objects.create(
        text_input= text,
        gemini_output= response.text
    )

    serializer = ChatBotSerializer(chatbot)
    
    return Response(serializer.data, status= status.HTTP_201_CREATED)