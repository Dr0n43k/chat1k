# Generated by Django 4.1.2 on 2022-10-27 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_message_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
