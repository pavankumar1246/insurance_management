from django.db import models
from django.contrib.auth.models import User
import datetime


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/Customer/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    health_report = models.FileField(upload_to='health_report/Customer/', null=True, blank=True)
    date_of_birth = models.DateField(default=datetime.date.today)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name