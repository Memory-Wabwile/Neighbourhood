from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    count = models.IntegerField()
    description = models.TextField()
    image = CloudinaryField('images')
    admin=models.ForeignKey(User,on_delete=models.CASCADE, related_name='admin') 
    health = models.IntegerField(null=True, blank=True)
    police = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    

class Profile(models.Model):
    name = models.CharField(max_length=100, blank =True )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) 
    user_id = models.IntegerField()
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField()
    profile_pic = CloudinaryField('images')
    bio = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class Business(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default = '')
    email = models.CharField(max_length=100, default = '')
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE, default='', null=True, blank=True)
    description = models.TextField( default = '')

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    post_image = CloudinaryField('images')
    post_description =models.TextField()
    user= models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    neighborhood=models.ForeignKey(Neighbourhood,on_delete= models.CASCADE,null=True)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title


    
