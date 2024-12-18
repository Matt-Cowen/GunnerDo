from django.db import models
from django.contrib.auth.models import User

STATUS = ((1, "League 1"), (2, "Championship"), (3, "Premiership"))
PROGRESS = ((1, "Locker Room"), (2, "Kick-off"), (3, "Full-time"))

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user"
    )
    name = models.CharField(max_length=200)
    notes = models.TextField(default="Tactics...", null=True, blank=True, max_length=300)
    progress = models.IntegerField(choices=PROGRESS, default=1)
    importance = models.IntegerField(choices=STATUS, default=2)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name