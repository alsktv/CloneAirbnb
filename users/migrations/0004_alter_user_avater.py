# Generated by Django 5.0.4 on 2024-04-12 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_avater_user_currency_user_gender_user_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avater',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]