from django.shortcuts import render
from rest_framework import viewsets
from titanic_app.serializers import titanicserializer
from rest_framework.response import Response
from titanic_app.models import titanic
from titanic_app.ml import pred
# Create your views here.



class viewsets_create(viewsets.ViewSet):
    http_method_names = ['post','get']

    def create(self,request):
        serializers=titanicserializer(data=request.data)
        if serializers.is_valid():


            serializers.save()
            ob=titanic.objects.latest('id')


            print(ob,'----------------------------------------')
            data=pred(ob)
            print(data)
            return Response({"survived" : data})
        else:
            return Response(serializers.errors)
