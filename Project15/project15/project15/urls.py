
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

# Creating the Router object
router = DefaultRouter()
#Note---->
#registering the Router and providing the basename 
#here studentapi is the preffix where the url is start form
# views.StudentViewSet: The ViewSet class handling logic for GET, POST, PUT, DELETE, etc.
#basename-> Used to generate the name of the URL patterns (student-list, student-detail, etc.) if the queryset is not provided in the ViewSet.
# router.register('studentapi/<int:pk>',views.StudentViewSet,basename='')
router.register('studentapi',views.StudentReadOnlyModelViewSet,basename = 'student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]


