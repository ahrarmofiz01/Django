from django.db import models
from django.utils import timezone

# Create your models here.
class appvarity(models.Model):
    APP_TYPE_CHOICE=[
        ('ml','masala'),
        ('gr','ginger'),
        ('nl','normal'),
        ('bt','belam'),
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='apps/')
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=APP_TYPE_CHOICE)

    def __str__(self):
       return self.name
