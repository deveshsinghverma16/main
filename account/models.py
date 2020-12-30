from django.db import models
from django.contrib.auth.models import User

class foodModel(models.Model):
    food_name = models.CharField(max_length=1000)
    food_price = models.IntegerField()
    food_description = models.TextField(max_length=1000000)
    food_image = models.FileField(upload_to='pics/',blank=True)

    def __str__(self):
        return self.food_name


class CartModel(models.Model):
    food_name = models.CharField(max_length=1000,blank=True)
    food_price = models.CharField(max_length=1000,blank=True)

    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username


class OrdersModel(models.Model):
    food_name = models.CharField(max_length=1000,blank=True)
    food_price = models.CharField(max_length=1000,blank=True)
    is_undelievered = models.BooleanField(default=True)
    is_delievered = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.user.username


    