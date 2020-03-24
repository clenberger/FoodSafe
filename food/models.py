from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class FoodItem(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    item_name = models.CharField(max_length=100)
    
    description = models.TextField(help_text="Write the desciption of your food item!")
    
    date_added = models.DateField(auto_now_add=True)
    
    date_expires = models.DateField()