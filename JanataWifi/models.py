from django.db import models
from django.core.validators import validate_comma_separated_integer_list

# # Create your models here.
# class Stock(models.Model):
#     trade_code = models.CharField(max_length=50)
#     date = models.DateField()
#     open = models.DecimalField(max_digits=10, decimal_places=2)
#     high = models.DecimalField(max_digits=10, decimal_places=2)
#     low = models.DecimalField(max_digits=10, decimal_places=2)
#     close = models.DecimalField(max_digits=10, decimal_places=2)
#     volume = models.CharField(max_length=100,validators=[validate_comma_separated_integer_list])
    
#     def __str__(self) -> str:
#         return self.trade_code
    

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
    
    
    


