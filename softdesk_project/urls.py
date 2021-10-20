from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#from projects.views import ProjectAPIView
from project.views import ProjectViewset #, AdminProjectViewset
from user.views import UserViewset, RegisterApi, CreateUserAPIView
from comment.views import CommentViewset
from issue.views import IssueViewset
from contributor.views import ContributorViewset


# création du routeur
router = routers.SimpleRouter()
# déclaration de project afin de générer l'URL correspondante
router.register('projects', ProjectViewset, basename='projects')
router.register('user', UserViewset, basename='user')
router.register('comment', CommentViewset, basename='comment')
router.register('issue', IssueViewset, basename='issue')
router.register('contributor', ContributorViewset, basename='contributor')

#router.register('admin/project', AdminProjectViewset, basename='admin-project')

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api-auth/', include('rest_framework.urls')),    
	path('login/', TokenObtainPairView.as_view(), name='obtain_tokens'),
	path('signup/', RegisterApi.as_view(), name='signup'),
	#path('signup/', CreateUserAPIView.as_view(), name='signup'),

	path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
	path('', include(router.urls)), # urls du router pour rendre les urls disponibles
	path('', include('user.urls')),
]


if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		path('__debug__/', include(debug_toolbar.urls)),
	] + urlpatterns

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
