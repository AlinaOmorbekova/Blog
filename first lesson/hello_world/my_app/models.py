from django.db import models

# Create your models here.
class About(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
    allow_mailing = models.BooleanField(default=False)