# Generated by Django 4.0.3 on 2022-03-29 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_confirmation_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
