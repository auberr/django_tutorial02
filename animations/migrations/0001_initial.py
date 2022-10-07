# Generated by Django 4.1.2 on 2022-10-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
            ],
            options={
                'db_table': 'genre',
            },
        ),
        migrations.CreateModel(
            name='Animation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=70)),
                ('original_title', models.CharField(default='', max_length=70)),
                ('company', models.CharField(default='', max_length=70)),
                ('rated', models.CharField(default='', max_length=70)),
                ('broadcasted_date', models.CharField(default='', max_length=70)),
                ('chapters', models.CharField(default='', max_length=70)),
                ('story', models.TextField(default='', max_length=256)),
                ('img', models.TextField(default='', max_length=256)),
                ('genre', models.ManyToManyField(related_name='animations', to='animations.genre')),
            ],
            options={
                'db_table': 'animation',
            },
        ),
    ]
