# Generated by Django 4.0.3 on 2022-03-29 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_email_confirmation_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reset_key_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
