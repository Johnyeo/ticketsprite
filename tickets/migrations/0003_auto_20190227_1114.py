# Generated by Django 2.1.5 on 2019-02-27 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20190227_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='session_key',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='openid',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='sid',
            field=models.CharField(default='', max_length=200),
        ),
    ]
