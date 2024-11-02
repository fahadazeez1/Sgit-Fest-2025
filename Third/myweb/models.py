from django.db import models
from django.core.exceptions import ValidationError
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
    
class Registration2(models.Model):
    name=models.CharField(max_length=78)
    email=models.EmailField(primary_key=True)
    dob=models.DateField()
    GAME_CHOICES = [
        ('jump', 'Long jump'),
        ('race', 'Race'),
        ('bb', 'Basket Ball'),
        ('crick', 'Cricket'),
    ]
    game = models.CharField(max_length=10, choices=GAME_CHOICES, default='jump')    
    def saves(self, *args, **kwargs):
        # Check for duplicate email
        if Registration2.objects.filter(email=self.email).exists() and not self.pk:
            raise ValidationError("This email is already registered.")
        super().save(*args, **kwargs)


class basket(models.Model):
    teamname=models.CharField(max_length=45,primary_key=True)
    mob=models.IntegerField()
    captain=models.CharField(max_length=45)
    # player1=models.CharField(max_length=45)
    player2=models.CharField(max_length=45)
    player3=models.CharField(max_length=45)
    player4=models.CharField(max_length=45)
    player5=models.CharField(max_length=45)
    player6=models.CharField(max_length=45)
    player7=models.CharField(max_length=45)
    player8=models.CharField(max_length=45)
    player9=models.CharField(max_length=45)
    player10=models.CharField(max_length=45)

