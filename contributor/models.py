from django.db import models, transaction
from django.conf import settings
from contributor.choices import *
from project.models import Project
from user.models import User


class Contributor(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.CharField(max_length=1, choices=PERMISSIONS_CHOICES, 
    	default=1)
    role = models.CharField(max_length=128)
    project_id = models.ForeignKey(Project, 
    	on_delete=models.CASCADE, related_name='contributor', default=None)

