# Generated by Django 5.0.4 on 2024-05-06 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_avater'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avater',
            field=models.URLField(blank=True, null=True),
        ),
    ]
