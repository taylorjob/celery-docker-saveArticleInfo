# Generated by Django 2.2.1 on 2019-09-04 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190904_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='article',
            name='urlToImage',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
