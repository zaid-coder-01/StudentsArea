from django.db import models


# Create your models here.

class Facts(models.Model):
    id = models.AutoField(primary_key=True)
    facts=models.TextField()

    def __str__(self):
        return self.facts
