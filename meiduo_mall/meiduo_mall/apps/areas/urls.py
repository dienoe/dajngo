from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter
urlpatterns=[

   ]
router=DefaultRouter()
router.register('areas',views.AreasViewSet,base_name='areas')
urlpatterns+=router.urls