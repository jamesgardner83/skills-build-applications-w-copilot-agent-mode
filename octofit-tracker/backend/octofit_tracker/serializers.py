from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'members']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'date']

class TeamNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']

class WorkoutSerializer(serializers.ModelSerializer):
    suggested_for = TeamNameSerializer(many=True, read_only=True)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'suggested_for']

class LeaderboardSerializer(serializers.ModelSerializer):
    team = TeamNameSerializer(read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'total_points']
