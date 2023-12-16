from django.db import models
from brand.models import Brand

# Create your models here.

class Car(models.Model):
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='car/media/uploads')
    title=models.TextField()
    description=models.TextField()
    quantity=models.IntegerField()
    price=models.IntegerField()
    
    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    car=models.ForeignKey(Car,on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=20)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f' Comment by {self.name}'