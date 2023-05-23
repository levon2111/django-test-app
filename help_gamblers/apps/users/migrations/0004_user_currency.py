# Generated by Django 4.0.3 on 2023-03-04 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('users', '0003_user_reset_key_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.currency'),
        ),
    ]
