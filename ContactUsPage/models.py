
from django.db import models


class Contactus(models.Model):
    Name = models.CharField(max_length=150,null=True)
    Email = models.EmailField(max_length=50,null=True)
    Message = models.TextField()
    created_at=models.DateField(auto_now_add=True)