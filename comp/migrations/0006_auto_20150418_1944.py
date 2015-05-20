# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0005_review_summary_company_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review_summary',
            name='company_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
