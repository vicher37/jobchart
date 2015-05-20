# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0002_auto_20150317_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='review_summary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=30)),
                ('part_of_speech', models.CharField(max_length=30)),
                ('frequency', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
