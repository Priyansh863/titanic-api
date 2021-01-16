from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class client_reate(models.Model):
    name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    phone_no=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    is_otp=models.CharField(max_length=100,null=True,blank=True)
class titanic(models.Model):
    PassengerId=models.CharField(max_length=100)
    Pclass=models.IntegerField()
    Age=models.CharField(max_length=100)
    Name=models.CharField(max_length=100)
    Sex=models.CharField(max_length=100)
    Fare=models.FloatField()
    Ticket=models.CharField(max_length=100)
    Cabin=models.CharField(max_length=100)
    Embarked=models.CharField(max_length=100)
    Survived=models.IntegerField(null=True,blank=True,default=1)
    SibSp=models.IntegerField(null=True,blank=True)
    Parch=models.IntegerField()
    def to_dict(self):
        return {
            'PassengerId' : self.PassengerId,
            'Pclass' : self.Pclass,
            'Age' : self.Age,
            'Sex' : self.Sex,
            'Fare' : self.Fare,
            'Ticket' : self.Ticket,
            'Cabin' : self.Cabin,
            'Embarked' : self.Embarked,
            'Survived' : self.Survived,
            'SibSp' : self.SibSp,
            'Parch' : self.Parch,
            'Name' : self.Name,
}


