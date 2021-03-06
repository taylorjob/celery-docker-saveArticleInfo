# Generated by Django 2.2.1 on 2019-09-03 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(blank=True, default='Unknown', max_length=30, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateTimeField(verbose_name='date published')),
                ('url', models.CharField(max_length=150)),
                ('urlToImage', models.CharField(blank=True, max_length=250, null=True)),
                ('avgImgColorR', models.IntegerField(null=True)),
                ('avgImgColorG', models.IntegerField(null=True)),
                ('avgImgColorB', models.IntegerField(null=True)),
                ('sentiment', models.DecimalField(decimal_places=4, max_digits=5, null=True)),
            ],
        ),
    ]
