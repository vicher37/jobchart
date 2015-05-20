# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0003_review_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='review_summary',
            name='company',
            field=models.CharField(max_length=30, default=1),
            preserve_default=False,
        ),
    ]
