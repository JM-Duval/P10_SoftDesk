from django.db import models
from django.conf import settings
from user.models import User 
from issue.models import Issue

class Comment(models.Model):

    description = models.CharField(max_length=128)
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    issue_id = models.ForeignKey(Issue, on_delete=models.CASCADE, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
