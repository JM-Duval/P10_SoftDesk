from django.db import models
from django.conf import settings

class Issue(models.Model):

	title = models.CharField(max_length=128)
	description = models.CharField(max_length=128)
	tag = models.CharField(max_length=128)
	priority = models.CharField(max_length=128)
	project_id = models.IntegerField(default=0)
	status = models.CharField(max_length=128)
	#author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, 
    #	on_delete=models.CASCADE)
	
	#author_user_id = models.ForeignKey('user.User', 
    #	on_delete=models.CASCADE)
	assignee_user_id = models.ForeignKey('user.User', 
    	on_delete=models.CASCADE)
	created_time = models.DateTimeField(auto_now_add=True)
