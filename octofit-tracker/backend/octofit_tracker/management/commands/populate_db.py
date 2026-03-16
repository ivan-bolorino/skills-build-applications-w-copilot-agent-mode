from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Limpa dados existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Times
        marvel = Team.objects.create(name='Marvel', description='Equipe Marvel')
        dc = Team.objects.create(name='DC', description='Equipe DC')

        # Usuários
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Atividades
        Activity.objects.create(user=users[0], type='Corrida', duration=30, date=date.today())
        Activity.objects.create(user=users[1], type='Ciclismo', duration=45, date=date.today())
        Activity.objects.create(user=users[2], type='Natação', duration=25, date=date.today())
        Activity.objects.create(user=users[3], type='Yoga', duration=40, date=date.today())

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        # Workouts
        Workout.objects.create(name='Treino Marvel', description='Treino especial para heróis Marvel', suggested_for='Marvel')
        Workout.objects.create(name='Treino DC', description='Treino especial para heróis DC', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('Banco populado com dados de teste!'))
