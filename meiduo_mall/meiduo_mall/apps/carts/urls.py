from django.conf.urls import url

from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
   url(r'^cart/$',views.CartView.as_view())
]
