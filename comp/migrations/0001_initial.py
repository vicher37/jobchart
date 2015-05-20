# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rating',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=30)),
                ('FB_likes', models.IntegerField(default=1)),
                ('FB_likes_score', models.IntegerField(default=1)),
                ('overall_rating', models.DecimalField(default=1, max_digits=3, decimal_places=2)),
                ('senior_leadership_rating', models.DecimalField(default=1, max_digits=3, decimal_places=2)),
                ('work_life_balance_rating', models.DecimalField(default=1, max_digits=3, decimal_places=2)),
                ('recommend_to_friend_rating', models.DecimalField(default=1, max_digits=3, decimal_places=2)),
                ('culture_and_values_rating', models.DecimalField(default=1, max_digits=3, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
