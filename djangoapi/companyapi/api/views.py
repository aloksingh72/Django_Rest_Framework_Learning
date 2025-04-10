from django.shortcuts import render

from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from  django.http import HttpResponse, JsonResponse




def student_details(request,pk):
    # creating the models instance
    stu = Student.objects.get(id =pk)
    # converting that instance into python dict
    serializer = StudentSerializer(stu)
    # render that data in JSON
    # json_data  = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type ='application/json')
    # to rmeove above two lines---^^
    return JsonResponse(serializer.data)


def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)

