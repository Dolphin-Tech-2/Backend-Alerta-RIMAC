from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

from .models import ChatBot
from .serializers import ChatBotSerializer

import google.generativeai as genai

# Create a generative model
genai.configure(api_key= 'AIzaSyD-QCHV_3TeGPknu_S2-SnjBfrIIUA5tfg')

# Create your views here.
@api_view(['POST'])
def chatbot(request):
    data = request.data
    
    text = data['text_input']
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat()
    response = chat.send_message(text)
    
    print(response.text)

    chatbot = ChatBot.objects.create(
        text_input= text,
        gemini_output= response.text
    )

    serializer = ChatBotSerializer(chatbot)
    
    return Response(serializer.data)