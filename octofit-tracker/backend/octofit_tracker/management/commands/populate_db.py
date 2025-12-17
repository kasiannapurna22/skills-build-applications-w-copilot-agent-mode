from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users (Superheroes)
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='password', team=dc),
        ]

        # Create Workouts
        workout1 = Workout.objects.create(name='Push Ups', description='Do 20 push ups')
        workout2 = Workout.objects.create(name='Running', description='Run 5km')
        workout3 = Workout.objects.create(name='Sit Ups', description='Do 30 sit ups')

        # Create Activities
        Activity.objects.create(user=users[0], workout=workout1, duration=10, calories=50)
        Activity.objects.create(user=users[1], workout=workout2, duration=30, calories=200)
        Activity.objects.create(user=users[2], workout=workout3, duration=15, calories=70)
        Activity.objects.create(user=users[3], workout=workout1, duration=12, calories=60)
        Activity.objects.create(user=users[4], workout=workout2, duration=28, calories=190)
        Activity.objects.create(user=users[5], workout=workout3, duration=18, calories=80)

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=90)
        Leaderboard.objects.create(user=users[2], score=80)
        Leaderboard.objects.create(user=users[3], score=95)
        Leaderboard.objects.create(user=users[4], score=85)
        Leaderboard.objects.create(user=users[5], score=75)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
