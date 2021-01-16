__author__ = 'PRIYANSH KHANDELWAL'
from rest_framework.routers import DefaultRouter
from titanic_app import views
from django.urls import path,include
from django.views.generic.base import RedirectView

router=DefaultRouter()
router.register(r'titanic',views.viewsets_create,basename='titanic')
urlpatterns=router.urls