from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS_CHOICES = (
        ('created', 'Created'),
        ('accepted', 'Accepted'),
        ('closed', 'Closed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
