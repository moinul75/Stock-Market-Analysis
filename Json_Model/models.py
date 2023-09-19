from django.db import models

# Create your models here.

class Stock(models.Model):
    trade_code = models.CharField(max_length=50)
    date = models.DateField()
    open = models.CharField(max_length=20)
    high = models.CharField(max_length=20)
    low = models.CharField(max_length=20)
    close = models.CharField(max_length=20)
    volume = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.trade_code