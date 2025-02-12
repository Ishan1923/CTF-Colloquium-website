from django.urls import path
from . import views

urlpatterns = [
    path('leaderboard/', views.UpdateTeamScore.as_view(), name = 'update_team_score'),
    path('leaderboard/list/', views.LeaderboardList.as_view(), name = 'leaderboard_list'),
    path('mleaderboard', views.leaderboard, name = 'leaderboard'),
    path('leaderboard/clear/', views.ClearLeaderboard.as_view(), name = 'clear_leaderboard'),
]