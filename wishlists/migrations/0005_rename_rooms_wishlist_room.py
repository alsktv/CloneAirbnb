# Generated by Django 5.0.4 on 2024-04-24 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlists', '0004_alter_wishlist_experience_alter_wishlist_rooms_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='rooms',
            new_name='room',
        ),
    ]
