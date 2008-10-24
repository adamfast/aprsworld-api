from django.db import models

class LastPosition(models.Model):
    packet_id = models.IntegerField(primary_key=True)
    packet_date = models.DateTimeField()
    source = models.CharField(max_length=9, primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    course = models.IntegerField(null=True, blank=True)
    speed = models.IntegerField(null=True, blank=True)
    altitude = models.IntegerField(null=True, blank=True)
    status = models.TextField(blank=True)
    symbol_table = models.CharField(max_length=1, blank=True)
    symbol_code = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = u'lastposition'

class Position(models.Model):
    packet_id = models.IntegerField(unique=True, primary_key=True)
    source = models.CharField(max_length=9)
    packet_date = models.DateTimeField()
    time_of_fix = models.IntegerField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    course = models.IntegerField(null=True, blank=True)
    speed = models.IntegerField(null=True, blank=True)
    altitude = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'position'
