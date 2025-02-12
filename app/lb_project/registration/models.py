from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        primary_key= True, 
        db_column = "user_id")
    username = models.CharField(max_length = 100, unique = False)
    rollno = models.IntegerField(default = 0, unique=True)
    mailid = models.EmailField(max_length=254)
    team_name = models.CharField(max_length = 100, unique = False)
    hostel = models.CharField(max_length = 10, unique = False)

    def __str__(self):
        return f"{self.user.username}'s Profile"

