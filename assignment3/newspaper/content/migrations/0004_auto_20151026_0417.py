# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_contributor_contents'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='house',
            field=models.CharField(default='Mather', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contributor',
            name='contents',
            field=models.ManyToManyField(related_name='contributor', to='content.Content', blank=True),
        ),
    ]
