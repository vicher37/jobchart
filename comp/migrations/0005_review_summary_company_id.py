# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0004_review_summary_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='review_summary',
            name='company_id',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
