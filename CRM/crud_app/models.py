from django.db import models

# Create your models here.
class CreateRecord(models.Model):
    date_create = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.id}-{self.first_name} {self.last_name}'