# Generated by Django 4.0.3 on 2023-02-26 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso', models.CharField(max_length=2)),
                ('iso3', models.CharField(max_length=3, unique=True)),
                ('iso_numeric', models.IntegerField(unique=True)),
                ('fips', models.CharField(blank=True, max_length=3, null=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('capital', models.CharField(blank=True, max_length=255, null=True)),
                ('area', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('population', models.IntegerField(blank=True, null=True)),
                ('continent', models.CharField(blank=True, max_length=2, null=True)),
                ('tld', models.CharField(blank=True, max_length=255, null=True)),
                ('currency_code', models.CharField(blank=True, max_length=3, null=True)),
                ('currency_symbol', models.CharField(blank=True, max_length=255, null=True)),
                ('currency_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code_format', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code_regex', models.CharField(blank=True, max_length=255, null=True)),
                ('languages', models.CharField(blank=True, max_length=255, null=True)),
                ('geonameid', models.IntegerField(blank=True, null=True)),
                ('neighbours', models.CharField(blank=True, max_length=255, null=True)),
                ('equivalent_fips_code', models.CharField(blank=True, max_length=4, null=True)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, verbose_name='code')),
                ('name', models.CharField(db_index=True, max_length=55, verbose_name='name')),
                ('symbol', models.CharField(blank=True, db_index=True, max_length=4, verbose_name='symbol')),
                ('factor', models.DecimalField(decimal_places=10, default=1.0, help_text='Specifies the currency rate ratio to the base currency.', max_digits=30, verbose_name='factor')),
                ('is_active', models.BooleanField(default=True, help_text='The currency will be available.', verbose_name='active')),
                ('is_base', models.BooleanField(default=False, help_text='Make this the base currency against which rate factors are calculated.', verbose_name='base')),
                ('is_default', models.BooleanField(default=False, help_text='Make this the default user currency.', verbose_name='default')),
                ('info', models.JSONField(blank=True, default=dict)),
            ],
            options={
                'verbose_name': 'currency',
                'verbose_name_plural': 'currencies',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Licence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'licences',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_639_1', models.CharField(max_length=2)),
                ('iso_639_2T', models.CharField(blank=True, max_length=3, unique=True)),
                ('iso_639_2B', models.CharField(blank=True, max_length=3, unique=True)),
                ('iso_639_3', models.CharField(blank=True, max_length=3)),
                ('name_en', models.CharField(max_length=100)),
                ('name_native', models.CharField(max_length=100)),
                ('family', models.CharField(max_length=50)),
                ('notes', models.CharField(blank=True, max_length=100)),
                ('countries_spoken', models.ManyToManyField(blank=True, to='core.country')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'ordering': ['name_en'],
            },
        ),
    ]
