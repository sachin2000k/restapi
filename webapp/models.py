from django.db import models

# Create your models here.
class employees(models.Model):
    username= models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    father_name=models.CharField(max_length=100)
    date_of_birth = models.DateField(default=None)
    age=models.CharField(max_length=23)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)

    def __str__(self):
        return self.username
