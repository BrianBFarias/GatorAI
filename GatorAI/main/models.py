from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Phone(models.Model):
    price = models.IntegerField(default=0)
    storage = models.IntegerField(default=0)
    cameras = models.IntegerField(default=0)
    model = models.CharField(default=0, max_length=100)

    TYPE = (
       ('apple', ('Iphone')),
       ('samsung', ('Galaxy')),
       ('Google', ('Pixel')),
      ('other', ('other')),

   )

    type = models.CharField(
       max_length=32,
       choices=TYPE,
       default='other',
   )
    
    def __str__(self):
        return f"{self.type} - {self.id}: {self.price}"
    
    def serialize(self):
        return{
            'id': self.id,
            'storage': self.storage,
            'type':self.type,
            'camera': self.cameras,
            'price': self.price,
            'model':self.model
        }

class Network(models.Model):
    rate = models.IntegerField(default=0)
    lines = models.IntegerField(default=0)
    data = models.IntegerField(default=0)

    TYPE = (
       ('mobile', ('mobile')),
       ('home', ('home')),
   )

    type = models.CharField(
       max_length=32,
       choices=TYPE,
       default='mobile',
   )
    
    def __str__(self):
        return f"{self.type} - {self.id}: {self.rate}"
    
    def serialize(self):
        return{
            'id': self.id,
            'rate': self.rate,
            'data':self.data,
            'lines': self.lines,
            'type': self.type,
        }