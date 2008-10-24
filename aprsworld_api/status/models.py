from django.db import models

class LastStatus(models.Model):
    packet_id = models.IntegerField(primary_key=True)
    packet_date = models.DateTimeField()
    source = models.CharField(max_length=9)
    comment = models.TextField(blank=True)
    power = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    gain = models.IntegerField(null=True, blank=True)
    directivity = models.IntegerField(null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True)
    symbol_table = models.CharField(max_length=1, blank=True)
    symbol_code = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = u'laststatus'

class Status(models.Model):
    packet_id = models.IntegerField(primary_key=True)
    source = models.CharField(max_length=9)
    comment = models.TextField(blank=True)
    power = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    gain = models.IntegerField(null=True, blank=True)
    directivity = models.IntegerField(null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True)
    symbol_table = models.CharField(max_length=1, blank=True)
    symbol_code = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = u'status'
