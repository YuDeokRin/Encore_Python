from django.db import models

class MyBoard(models.Model):
    myname = models.CharField(max_length=200)
    mytitle = models.CharField(max_length=500)
    mycontent = models.CharField(max_length=2000)
    mydate = models.DateTimeField('data published')
    
