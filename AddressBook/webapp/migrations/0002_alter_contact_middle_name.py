# Generated by Django 3.2.5 on 2021-07-19 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='middle_name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
