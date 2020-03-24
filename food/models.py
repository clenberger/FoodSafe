from django.db import models


# Create your models here.
class FoodItem(models.Model):
    
    item_name = models.CharField(max_length=100)
    
    description = models.TextField(help_text="Write the desciption of your food item!")
    
    date_added = models.DateField(auto_now_add=True)
    
    date_expires = models.DateField()