from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TeamScore
from .serializers import TeamScoreSerializer
from django.views import View
from django.http import JsonResponse
from .models import TeamScore

# Create your views here.


#Endpoint to update or create a team's score

class UpdateTeamScore(APIView):
    def post(self, request, format = None):
        team_name = request.data.get('team_name')
        score = request.data.get('score')

        if team_name is None or score is None:
            return Response({'error' : 'team_name and score are required'}, status=status.HTTP_400_BAD_REQUEST)
        

        team_score, created = TeamScore.objects.update_or_create(
            team_name = team_name,
            defaults={'score' : score}
        )
        serializer = TeamScoreSerializer(team_score)
        


        return Response(serializer.data, status = status.HTTP_200_OK)
    

class LeaderboardList(generics.ListAPIView):
    serializer_class = TeamScoreSerializer

    def get_queryset(self):
        return TeamScore.objects.all().order_by('-score')
    
def leaderboard(request):
    return render(request, 'website/leaderboard.html')

class ClearLeaderboard(View):
    def delete(self, request, *args, **kwargs):
        TeamScore.objects.all().delete()
        return JsonResponse({"message": "Leaderboard cleared successfully!"}, status=200)