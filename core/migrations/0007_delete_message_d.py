# Generated by Django 3.2.4 on 2022-03-23 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_message_message_d'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message_d',
        ),
    ]
