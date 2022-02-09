from celery import shared_task
from main.models import UserProfile
from app.celery import app

@app.task(bind=True)
def check_flag(self):
    self.users = UserProfile.objects.filter(is_notified=False)
    for user in self.users:
        user.is_notified = True
        user.save()



