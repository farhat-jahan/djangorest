from django.db import models
from django.utils import timezone
import datetime

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Stock(BaseModel):
    ticker= models.CharField(max_length=10)
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    
    def __str__(self):
        return self.ticker
    
    class Meta:
        db_table = "stock"

