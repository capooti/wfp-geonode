# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-21 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('layers', '0033_auto_20180606_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='name by which the cited training is known', max_length=255, verbose_name='title')),
                ('logo', models.ImageField(upload_to=b'trainings/logos')),
                ('manual', models.FileField(upload_to=b'trainings/manuals')),
                ('publication_date', models.DateField(help_text='publication date of the training', verbose_name='publication date')),
                ('abstract', models.TextField(blank=True, help_text='brief narrative summary of the content of the training', verbose_name='abstract')),
                ('keywords', taggit.managers.TaggableManager(blank=True, help_text='commonly used word(s) or formalised word(s) or phrase(s) used to describe the subject (space or comma-separated', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='keywords')),
                ('layers', models.ManyToManyField(blank=True, to='layers.Layer')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name_plural': 'GIS Trainings',
            },
        ),
    ]
