from urllib.request import urlopen
from xmlrpc.client import boolean
from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
   #id = models.
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)
