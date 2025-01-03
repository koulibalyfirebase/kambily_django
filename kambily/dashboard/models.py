from django.db import models

# Create your models here.
class Report(models.Model):
    admin = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

class Statistic(models.Model):
    key = models.CharField(max_length=100)
    value = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
