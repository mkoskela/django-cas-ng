# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyGrantingTicket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pgtiou', models.CharField(max_length=255, null=True, blank=True)),
                ('pgt', models.CharField(max_length=255, null=True, blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('session', models.ForeignKey(related_name='+', blank=True, to='sessions.Session', null=True)),
                ('user', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SessionTicket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticket', models.CharField(max_length=255)),
                ('session', models.OneToOneField(related_name='+', to='sessions.Session')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='proxygrantingticket',
            unique_together=set([('session', 'user')]),
        ),
    ]
