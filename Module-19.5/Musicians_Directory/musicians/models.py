from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email=models.EmailField()
    phone_no=models.CharField(max_length=20)
    instrument_type=models.CharField(max_length=200)
     
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name