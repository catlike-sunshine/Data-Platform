# Generated by Django 2.2.2 on 2019-06-25 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='article',
        ),
        migrations.DeleteModel(
            name='comment',
        ),
    ]
