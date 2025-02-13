from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.permissions import AllowAny  # Import AllowAny permission
from .models import TeamScore
from .serializers import TeamScoreSerializer

class UpdateTeamScore(APIView):
    permission_classes = [AllowAny]  # Allow unauthorized access

    def post(self, request):
        team_name = request.data.get('team_name')
        score = request.data.get('score')

        if not team_name or score is None:
            return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

        team, created = TeamScore.objects.update_or_create(
            team_name=team_name, defaults={"score": score}
        )
        return Response({"message": "Score updated successfully"}, status=status.HTTP_200_OK)

class LeaderboardList(ListAPIView):
    permission_classes = [AllowAny]  # Allow unauthorized access
    queryset = TeamScore.objects.order_by('-score')
    serializer_class = TeamScoreSerializer
