from django.db import models
from datetime import datetime
# Create your models here.
class SendMesg(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
    allow_mailing = models.BooleanField(default=False)

def article_directory_path(instance, filename):
    return 'static/{0}/{1}'.format(datetime.today().strftime('%Y-%m-%d'),filename)    
class CreateArticle(models.Model):
    title = models.CharField(max_length=100)  
    short_description = models.CharField(max_length=300, null=True)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to = article_directory_path ,null = True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
