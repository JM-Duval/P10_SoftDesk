from django.db import models
from django.conf import settings

class Comment(models.Model):

    comment_id = models.IntegerField(default=0)
    description = models.CharField(max_length=128)
    author_user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    issue_id = models.ForeignKey('issue.Issue', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    #author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, 
    #   on_delete=models.CASCADE)