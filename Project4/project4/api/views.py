from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators  import method_decorator
from django.views import View

# Create your views here.

#   -------------- CLASS BASED VIEW IN DJANGO ----------

@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body # recieving the data
        stream = io.BytesIO(json_data)   #steam implementation
        pythondata = JSONParser().parse(stream) #convert it into python data types
        id = pythondata.get('id',None)  #if id is passed in the json otherwise None
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer  = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type = 'application/json')
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type = 'application/json')
    
    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data created successfully!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')
    def put(self,request,*args,**kwargs):
        json_data  = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu,data = pythondata,partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data updated successfully!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'applicaton/json')
    
    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {'msg':'Data Deleted successfully!'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type = 'application/json')
        #to reduct the above two lines--^^ we also write JsonResponse
        return JsonResponse(res,safe = False)








