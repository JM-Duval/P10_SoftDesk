from django.db import models, transaction
from django.conf import settings

class Project(models.Model):

    project_id = models.IntegerField(default=0)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    type_project = models.CharField(max_length=128, default=None)
    author_user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)


    def __str__(self):
        return self.title