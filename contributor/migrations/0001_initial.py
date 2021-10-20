# Generated by Django 3.2.8 on 2021-10-18 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('project_id', models.IntegerField(default=0)),
                ('permission', models.CharField(choices=[(1, 'ACTEUR'), (2, 'ACCESSOIRISTE'), (3, 'ANIMATEUR 3D'), (4, 'ASSISTANT MONTEUR'), (5, 'ASSISTANT REALISATEUR'), (6, 'BRUITEUR')], default=1, max_length=1)),
                ('role', models.CharField(max_length=128)),
            ],
        ),
    ]
