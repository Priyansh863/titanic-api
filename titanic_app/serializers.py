__author__ = 'PRIYANSH KHANDELWAL'
from rest_framework import serializers
from django.contrib.auth.models import User
from titanic_app.models import titanic
class UserSerializer(serializers.ModelSerializer):
    #id = serializers.CharField(source='pk', read_only=True)
    class Meta:
        model = User
        fields = ('username','email')


class titanicserializer(serializers.ModelSerializer):
    #id = serializers.CharField(source='pk', read_only=True)
    class Meta:
        model = titanic
        fields = ('PassengerId',
            'Pclass' ,
            'Age',
            'Sex',
            'Fare',
            'Ticket',
            'Cabin',
            'Embarked',
            'Survived',
            'SibSp',
            'Parch',
            'Name'  )
