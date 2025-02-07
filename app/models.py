from django.db import models

# Create your models here.
class Task(models.Model):

    STATUS_CHOICES = [
        (1, 'to do'),
        (2, 'on going'),
        (3, 'done'),
    ]
    
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=True)
    date = models.DateField(null=False, blank=False)
    status = models.IntegerField(choices=STATUS_CHOICES, null=False, blank=False)
    
    def __str__(self):
        return self.title
    
    