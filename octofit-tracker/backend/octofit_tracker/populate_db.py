import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

# Create Teams
t1 = Team.objects.create(name='Alpha Team')
t2 = Team.objects.create(name='Beta Team')

# Create Users
u1 = User.objects.create(username='alice', email='alice@example.com', first_name='Alice', last_name='Smith', team=t1)
u2 = User.objects.create(username='bob', email='bob@example.com', first_name='Bob', last_name='Brown', team=t1)
u3 = User.objects.create(username='carol', email='carol@example.com', first_name='Carol', last_name='Jones', team=t2)

# Add members to teams
t1.members.add(u1, u2)
t2.members.add(u3)

# Create Workouts
w1 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio', difficulty='Hard', suggested_for='Weight Loss')
w2 = Workout.objects.create(name='Yoga Flow', description='Relaxing yoga session', difficulty='Easy', suggested_for='Flexibility')

# Create Activities
Activity.objects.create(user=u1, activity_type='Running', duration=30, calories_burned=300, date='2025-09-25')
Activity.objects.create(user=u2, activity_type='Cycling', duration=45, calories_burned=400, date='2025-09-25')
Activity.objects.create(user=u3, activity_type='Yoga', duration=60, calories_burned=200, date='2025-09-25')

# Create Leaderboard
Leaderboard.objects.create(team=t1, total_points=700, rank=1)
Leaderboard.objects.create(team=t2, total_points=200, rank=2)

print('Test data populated successfully.')