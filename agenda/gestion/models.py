from curses.ascii import NUL
from pyexpat import model
from django.db import models

class Etiqueta(models.Model):
    id = models.AutoField(primary_key=True,unique=True,null=False)
    nombre = models.CharField(max_length=20,unique=True,null=False)
    createdAt=models.DateTimeField(auto_now_add=True,db_column='created_at')
    updatedAt=models.DateTimeField(auto_now=True,db_column='updated_at')



    class Meta:
        db_table = 'etiquetas'
        ordering = ['-nombre']
