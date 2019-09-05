from django.db import models

class LoginUser(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length = 32)

    username = models.CharField(max_length = 32,null = True,blank = True)
    phone_number = models.CharField(max_length = 11,null = True,blank = True)
    photo = models.ImageField(upload_to = "images",null = True,blank = True)
    age = models.IntegerField(null = True,blank = True)
    gender = models.CharField(max_length = 32,null = True,blank = True)
    address = models.TextField(null = True,blank = True)

class Goods(models.Model):
    goods_number = models.CharField(max_length=11)
    goods_name = models.CharField(max_length=32)
    goods_price = models.FloatField()
    goods_count = models.IntegerField()
    goods_location = models.CharField(max_length=254)
    goods_safe_date = models.IntegerField()
    goods_pro_time = models.DateField(auto_now=True)
    goods_status = models.IntegerField() #0为下架，1 为在售
# Create your models here.
