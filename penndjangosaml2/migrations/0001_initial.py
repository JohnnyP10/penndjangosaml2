# Generated by Django 2.1.3 on 2018-11-16 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LongGroupName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.TextField()),
                ('count', models.IntegerField()),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]