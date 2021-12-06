# Generated by Django 3.2.8 on 2021-12-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('grade', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'Drf_Member_Table',
            },
        ),
    ]
