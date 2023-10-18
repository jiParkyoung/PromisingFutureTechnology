# Generated by Django 4.0.3 on 2022-05-16 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='link',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=2000, null=True)),
                ('URL', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'LINK',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='market',
            fields=[
                ('key', models.CharField(blank=True, max_length=200, null=True, primary_key=True, serialize=False)),
                ('contents', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'MARKETABILITY',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ThesisUse',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=1280, null=True)),
                ('year', models.CharField(max_length=1000)),
                ('month', models.CharField(max_length=1000)),
                ('use', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'thesis_use',
                'managed': False,
            },
        ),
    ]