# Generated by Django 2.2.4 on 2021-06-24 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_ingredient_chef'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(default='unit', max_length=25),
            preserve_default=False,
        ),
    ]
