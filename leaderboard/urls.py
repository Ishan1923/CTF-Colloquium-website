from django.urls import path
from .views import UpdateTeamScore, LeaderboardList, leaderboard

urlpatterns = [
    path('update-score/', UpdateTeamScore.as_view(), name='update-score'),
    path('leaderboard/', LeaderboardList.as_view(), name='leaderboard'),
    path('leaderboardview/', leaderboard, name='leaderboardview'),
]
