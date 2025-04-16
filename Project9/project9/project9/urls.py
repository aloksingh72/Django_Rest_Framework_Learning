from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.StudentAPI.as_view()), #some changes in the urls.py  for class based view
    path('studentapi/<int:pk>',views.StudentAPI.as_view()),
]