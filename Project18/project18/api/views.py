from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .custompermissions import MyPermission


# here we are gone to implement the SessionAuthentication along with various permission classes 
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class  = StudentSerializer
    authentication_classes = [SessionAuthentication]
    #Note:-> here we impelement the CustomPermissions
#here we import the custom permission and use it defined in the custompermssion.py file
    permission_classes = [MyPermission]






