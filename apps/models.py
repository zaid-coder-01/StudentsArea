from django.db import models
from datetime import date


# Create your models here.

class Facts(models.Model):
    id = models.AutoField(primary_key=True)
    facts = models.TextField()

    def __str__(self):
        return self.facts


class Document(models.Model):
    name = models.CharField(primary_key=True,max_length=200)
    document = models.FileField(upload_to="document/",unique=True)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.name
