from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', description='Desc')
        self.assertEqual(team.name, 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team', description='Desc')
        user = User.objects.create(name='Test User', email='test@user.com', team=team)
        self.assertEqual(user.email, 'test@user.com')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team', description='Desc')
        user = User.objects.create(name='Test User', email='test@user.com', team=team)
        activity = Activity.objects.create(user=user, type='Run', duration=30, date='2026-03-16')
        self.assertEqual(activity.type, 'Run')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team', description='Desc')
        leaderboard = Leaderboard.objects.create(team=team, points=50)
        self.assertEqual(leaderboard.points, 50)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Workout', description='Desc', suggested_for='Test')
        self.assertEqual(workout.name, 'Workout')
