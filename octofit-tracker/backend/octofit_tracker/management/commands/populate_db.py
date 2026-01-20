from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create Workouts
        workout1 = Workout.objects.create(name='Super Strength', description='Strength training for heroes')
        workout2 = Workout.objects.create(name='Agility Training', description='Agility and reflexes')
        workout1.suggested_for.set([marvel, dc])
        workout2.suggested_for.set([marvel, dc])

        # Create Activities
        Activity.objects.create(user=users[0], activity_type='Web Swinging', duration=30, date=timezone.now())
        Activity.objects.create(user=users[1], activity_type='Suit Up', duration=45, date=timezone.now())
        Activity.objects.create(user=users[2], activity_type='Lasso Practice', duration=40, date=timezone.now())
        Activity.objects.create(user=users[3], activity_type='Gadget Training', duration=50, date=timezone.now())

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, total_points=100)
        Leaderboard.objects.create(team=dc, total_points=90)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
