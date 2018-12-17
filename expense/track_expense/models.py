from django.db import models

# Create your models here.
class expense(models.Model):
    expense_name = models.CharField(max_length=30)
    price = models.FloatField()
    expense_image = models.FileField()
    created_date = models.DateTimeField(auto_now_add=True)