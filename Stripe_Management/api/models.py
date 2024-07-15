from django.db import models
from datetime import date
class Account(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    created = models.DateTimeField(default=date.today)
    
    def __str__(self):
        return self.name
