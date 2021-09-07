from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=300, blank=True)

    def __str__(self):
            return self.first_name

# class Picture(models.Model):
#     image = models.ImageField(upload_to= 'pictures/')
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=50)
#     location = models.ForeignKey('Location',on_delete = models.CASCADE,default=None)
#     category = models.ForeignKey('Category', on_delete = models.CASCADE,default=None)
#     author = models.ForeignKey(Author,on_delete = models.CASCADE)

class Location(models.Model):
    location_name = models.CharField(max_length=80)

class Category(models.Model):
    category_name = models.CharField(max_length=80)