from django.db import models

class TeamScore(models.Model):
    team_name = models.CharField(max_length=255, unique=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team_name}: {self.score}"
