from django.db import models, transaction
from django.conf import settings
from contributor.choices import *

class Contributor(models.Model):

    user_id = models.IntegerField(default=0)
    project_id = models.IntegerField(default=0)
    permission = models.CharField(max_length=1, choices=PERMISSIONS_CHOICES, default=1)
    role = models.CharField(max_length=128)

    def __str__(self):
        return self.title
