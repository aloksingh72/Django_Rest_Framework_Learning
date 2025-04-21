
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

# Creating the Router object
router = DefaultRouter()
#registering the Router and providing the basename 
router.register('studentapi',views.StudentViewSet,basename = 'student')
# router.register('studentapi/<int:pk>',views.StudentViewSet,basename='')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
