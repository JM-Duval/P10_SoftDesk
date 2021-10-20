from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from projects.models import Project

UserModel = get_user_model()


PROJECTS = [
    {
        'title': 'Moto GP Project',
        'description': 'GP 22',
        'type' : 'engineering',
    }
]


#ADMIN_ID = 'jmd3'
#ADMIN_PASSWORD = 'jmd3'


class Command(BaseCommand):

    help = 'Initialize project for local development'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))

        Project.objects.all().delete()

        for data_project in PROJECTS:
            project = Project.objects.create(title=data_project['title'],
                                             description=data_project['description'],
                                             types=data_project['type']
                                             )
            """
            for data_product in data_project['products']:
                product = category.products.create(name=data_product['name'],
                                                   active=data_product['active'])
                
                for data_article in data_product['articles']:
                    product.articles.create(name=data_article['name'],
                                            active=data_article['active'],
                                            price=data_article['price'])
                                    """
        #UserModel.objects.create_superuser(ADMIN_ID, 'admin@oc.drf', ADMIN_PASSWORD)

        self.stdout.write(self.style.SUCCESS("All Done !"))
