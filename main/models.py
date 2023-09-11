from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)  # Nama item dengan tipe CharField
    amount = models.IntegerField()           # Jumlah item dengan tipe IntegerField
    description = models.TextField()         # Deskripsi item dengan tipe TextField
