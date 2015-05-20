# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ratings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('company', models.CharField(max_length=30)),
                ('FB_likes', models.IntegerField(default=1)),
                ('FB_likes_score', models.DecimalField(decimal_places=2, max_digits=3, default=1)),
                ('overall_rating', models.DecimalField(decimal_places=2, max_digits=3, default=1)),
                ('senior_leadership_rating', models.DecimalField(decimal_places=2, max_digits=3, default=1)),
                ('work_life_balance_rating', models.DecimalField(decimal_places=2, max_digits=3, default=1)),
                ('recommend_to_friend_rating', models.DecimalField(decimal_places=2, max_digits=3, default=1)),
                ('culture_and_values_rating', models.DecimalField(decimal_places=2, max_digits=3, default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='rating',
        ),
    ]
