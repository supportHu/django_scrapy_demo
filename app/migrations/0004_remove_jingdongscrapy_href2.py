# Generated by Django 2.2.1 on 2019-06-28 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_jingdongscrapy_href2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jingdongscrapy',
            name='href2',
        ),
    ]
