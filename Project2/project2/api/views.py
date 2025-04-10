from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#Note :- what is the BytesIO() here it is usef to creating an in-memory stream (like a file so that it can be processed further) 
#  Because parsers like Django REST Framework's JSONParser expect a stream object to parse from — not raw bytes or strings.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
import io
@csrf_exempt
def student_create(request):
    if request.method == "POST":
        try:
            stream = io.BytesIO(request.body)
            pythondata = JSONParser().parse(stream)
            serializer = StudentSerializer(data=pythondata)
            
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'msg': 'Data Created', 'data': serializer.data}, status=201)
            return JsonResponse(serializer.errors, status=400)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)