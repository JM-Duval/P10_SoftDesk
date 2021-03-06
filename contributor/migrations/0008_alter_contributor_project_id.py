# Generated by Django 3.2.8 on 2021-10-29 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_author_user_id'),
        ('contributor', '0007_delete_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='project_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='contributor', to='project.project'),
        ),
    ]
