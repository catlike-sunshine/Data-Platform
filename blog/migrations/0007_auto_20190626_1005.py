# Generated by Django 2.1.5 on 2019-06-26 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_terms_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='terms',
            name='source',
            field=models.TextField(blank=True, verbose_name='词条来源'),
        ),
        migrations.AlterField(
            model_name='terms',
            name='content',
            field=models.TextField(verbose_name='词条说明'),
        ),
        migrations.AlterField(
            model_name='terms',
            name='title',
            field=models.CharField(max_length=200, verbose_name='概词条念'),
        ),
    ]
