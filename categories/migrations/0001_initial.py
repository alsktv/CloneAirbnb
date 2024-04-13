# Generated by Django 5.0.4 on 2024-04-13 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(choices=[('room', 'Room'), ('experience', 'Experience')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
