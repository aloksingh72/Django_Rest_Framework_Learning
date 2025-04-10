from django.contrib import admin
from .models import Student
# here we have to registered our admin
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','rollno','city']