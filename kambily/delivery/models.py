from django.db import models

# Create your models here.
class Mission(models.Model):
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    deliverer = models.ForeignKey('accounts.DelivererProfile', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('assigned', 'Assignée'), ('in_progress', 'En cours'), ('completed', 'Terminée')])
    assigned_at = models.DateTimeField(auto_now_add=True)
