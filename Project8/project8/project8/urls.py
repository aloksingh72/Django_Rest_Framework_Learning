from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.student_api), #some changes in the urls.py  for class based view
    path('studentapi/<int:pk>',views.student_api)
]