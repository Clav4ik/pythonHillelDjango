from celery import shared_task
from main.models import UserProfile
from app.celery import app

@app.task()
def check_flag():

    users = UserProfile.objects.filter(is_notified=False)
    for user in users:
        user.is_notified = True
        user.save()
    return 1

