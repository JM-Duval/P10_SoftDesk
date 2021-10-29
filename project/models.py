from django.db import models, transaction
from django.conf import settings
from user.models import User
#from contributor.models import Contributor

class Project(models.Model):

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    type_project = models.CharField(max_length=128, default=None)
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    #contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE, related_name='contributor', blank=True, null=True)
    #author_user_id = models.ForeignKey(default=User, on_delete=models.CASCADE)
    #author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, 
    #	on_delete=models.CASCADE)
    #project_id = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title