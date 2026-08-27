from django.db import models
from django.utils import timezone
from django.contrib.auth.models import user

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
    
#one to many

class AppReview(models.Model):
    app= models.ForeignKey(appvarity,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)


    def __str__(self):
       return f'{self.user.username} review{self.app.name}'
#MANY TO MANY
