# Generated by Django 4.2.6 on 2024-01-17 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='num_stars',
            field=models.IntegerField(choices=[(1, 'Worst'), (2, 'Bad'), (3, 'Not Bad'), (4, 'Good'), (5, 'Excellent!')]),
        ),
    ]