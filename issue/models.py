from django.db import models
from django.conf import settings
from issue.choices import TAG_CHOICES, PRIORITY_CHOICES, STATUS_CHOICES
from user.models import User
from project.models import Project


class Issue(models.Model):

	title = models.CharField(max_length=128)
	description = models.CharField(max_length=128)
	tag = models.CharField(max_length=1, choices=TAG_CHOICES, default=1)
	priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, 
		default=1)
	project_id = models.ForeignKey(Project, 
    	on_delete=models.CASCADE, related_name='issue')
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=1)
	assignee_user_id = models.ForeignKey(User, 
    	on_delete=models.CASCADE)
	created_time = models.DateTimeField(auto_now_add=True)


