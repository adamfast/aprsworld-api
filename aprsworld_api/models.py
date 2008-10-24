# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

# ? app
class LastUserDefined(models.Model):
    packet_id = models.IntegerField(primary_key=True)
    source = models.CharField(max_length=10)
    packet_date = models.DateTimeField()
    user_id = models.CharField(max_length=1)
    packet_type = models.CharField(max_length=1)
    information = models.TextField()
    class Meta:
        db_table = u'lastuserdefined'

# ? app
class QaHosts(models.Model):
    id = models.IntegerField(primary_key=True)
    host = models.CharField(max_length=255)
    active = models.IntegerField()
    class Meta:
        db_table = u'qa_hosts'

# ? app
class WatchPrograms(models.Model):
    program = models.IntegerField(unique=True, primary_key=True)
    user = models.CharField(max_length=20, blank=True)
    directory = models.TextField(blank=True)
    command = models.TextField()
    class Meta:
        db_table = u'watch_programs'

# ? app
class WatchUsers(models.Model):
    source = models.CharField(max_length=9, primary_key=True)
    program = models.IntegerField()
    class Meta:
        db_table = u'watch_users'
