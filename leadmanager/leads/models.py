from django.db import models

# Create your models here.
class Subordinate(models.Models):               #naming convention of table-> Capital first letter, Singular number
    name=models.CharField(max_length=50)        # first column
    emali=models.EmailField(max_length=80,unique=True)
    designation=models.CharField(max_length=50,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    




