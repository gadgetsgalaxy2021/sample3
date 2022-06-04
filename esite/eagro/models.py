from asyncio.windows_events import NULL
from django.db import models

from django.contrib.auth.models import AbstractUser


class signupUser(AbstractUser):
    sfullname=models.CharField(max_length=30)
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=100)
    semailid=models.EmailField(max_length=30)
    smobile=models.CharField(max_length=14)
    sdob=models.DateField(null=True)
    scountry=models.CharField(max_length=30,null=True)
    # is_superuser=models.BooleanField(default=False)
    # is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_authenticated=True
    is_anonymous=False
    USERNAME_FIELD='username'
    # REQUIRED_FIELDS=['username']
    # user_permissions=None

    def __str__(self):
        return self.username
    
    
    def get_username(self):
        return self.username
    
class product(models.Model):
    id=models.AutoField(primary_key=True)
    product_uname=models.CharField(max_length=50,default="admin")
    product_name=models.CharField(max_length=50)
    product_icon=models.ImageField(upload_to='images/')
    product_price=models.FloatField()
    product_quantity=models.IntegerField()
    product_desc=models.CharField(max_length=500)
    product_category=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.product_name
    
class usercart(models.Model):
    cprod_id=models.IntegerField()
    cprod_size=models.CharField(max_length=20,default=NULL)
    cusername=models.CharField(max_length=50)
    cproduct_name=models.CharField(max_length=50)
    cproduct_price=models.FloatField()
    cproduct_desc=models.CharField(max_length=300)
    cproduct_cat=models.CharField(max_length=30,default=NULL)

    def __str__(self):
        return self.cusername+" "+self.cproduct_name

# class availsize(models.Model):
#     aprod_category=models.BooleanField()
#     afivehundreadg=models.BooleanField()
#     aonwkg=models.BooleanField()
#     afivekg=models.BooleanField()

class order(models.Model):
    oprod_id=models.IntegerField()
    oprod_size=models.CharField(max_length=20)
    ousername=models.CharField(max_length=50)
    oproduct_name=models.CharField(max_length=50)
    oproduct_price=models.FloatField()
    # oproduct_desc=models.CharField(max_length=300)
    oproduct_cat=models.CharField(max_length=30)
    ouser_address=models.CharField(max_length=200)
    ouser_mobile=models.CharField(max_length=14)

