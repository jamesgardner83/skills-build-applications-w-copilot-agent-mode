from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', description='desc')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(name='U', email='u@test.com', team=team)
        self.assertEqual(str(user), 'U')

    def test_activity_creation(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(name='U', email='u@test.com', team=team)
        activity = Activity.objects.create(user=user, activity_type='Run', duration=10, date='2026-01-20')
        self.assertEqual(str(activity), 'U - Run')

    def test_workout_creation(self):
        team = Team.objects.create(name='T', description='d')
        workout = Workout.objects.create(name='W', description='desc')
        workout.suggested_for.set([team])
        self.assertEqual(str(workout), 'W')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='T', description='d')
        leaderboard = Leaderboard.objects.create(team=team, total_points=5)
        self.assertEqual(str(leaderboard), 'T Leaderboard')
