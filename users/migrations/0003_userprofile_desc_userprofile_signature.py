# Generated by Django 4.2.1 on 2023-06-09 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_emailverifyrecord_alter_userprofile_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='desc',
            field=models.TextField(blank=True, default='', max_length=200, verbose_name='个人简介'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='signature',
            field=models.CharField(blank=True, default='这个人什么也没有留下!(>_<)', max_length=200, verbose_name='签名'),
        ),
    ]
