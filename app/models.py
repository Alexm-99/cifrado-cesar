from django.db import models

# Create your models here.

class cifrado(models.Model):
    id = models.AutoField( primary_key=True)
    nickname = models.CharField(max_length=100) # codigo de menu
    message = models.CharField(max_length=500)
    key = models.CharField(max_length=200)
  

    def __str__(self):
        return self.id