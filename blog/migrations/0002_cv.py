# Generated by Django 2.2.12 on 2020-05-31 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_info', models.TextField()),
                ('education', models.TextField()),
                ('work_experience', models.TextField()),
            ],
        ),
    ]