from django.urls import path
from .views import UpdateTeamScore, LeaderboardList

urlpatterns = [
    path('update-score/', UpdateTeamScore.as_view(), name='update-score'),
    path('leaderboard/', LeaderboardList.as_view(), name='leaderboard'),
]
