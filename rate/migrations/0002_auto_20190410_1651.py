# Generated by Django 2.2 on 2019-04-10 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Star',
        ),
        migrations.AddField(
            model_name='post',
            name='star_rate',
            field=models.CharField(choices=[(100, '5'), (80, '4'), (60, '3'), (40, '2'), (20, '1'), (0, '0')], default=0, max_length=3),
        ),
    ]
