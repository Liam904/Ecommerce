# Generated by Django 5.0.2 on 2024-03-24 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationmessage',
            old_name='conversaton',
            new_name='conversation',
        ),
    ]
