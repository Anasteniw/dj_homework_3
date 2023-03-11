from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=15, decimal_places=2)
    image=models.ImageField(upload_to='images/')
    release_date=models.DateField()
    lte_exists= models.BooleanField(default=True)
    slug=models.SlugField(max_length = 50, unique=True)
    
   