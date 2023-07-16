from django.db import models

# Create your models here.
class Tracker(models.Model):
    id = models.IntegerField(primary_key=True)
    buy = models.IntegerField()
    reason = models.CharField(max_length=100,null=True)


class accounts(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50,null=True)
    amount = models.IntegerField(default=0)
