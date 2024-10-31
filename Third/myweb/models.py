from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=78)
    email=models.EmailField()
    dob=models.DateField()
    GAME_CHOICES = [
        ('jump', 'Long jump'),
        ('race', 'Race'),
        ('bb', 'Basket Ball'),
        ('crick', 'Cricket'),
    ]
    game = models.CharField(max_length=10, choices=GAME_CHOICES, default='jump')
    