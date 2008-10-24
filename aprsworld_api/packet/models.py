from django.db import models

class Raw(models.Model):
    packet_id = models.IntegerField(unique=True, primary_key=True)
    packet_time = models.IntegerField()
    ip_source = models.CharField(max_length=255, blank=True)
    source = models.CharField(max_length=9)
    destination = models.CharField(max_length=9)
    digipeater_0 = models.CharField(max_length=9, blank=True)
    digipeater_1 = models.CharField(max_length=9, blank=True)
    digipeater_2 = models.CharField(max_length=9, blank=True)
    digipeater_3 = models.CharField(max_length=9, blank=True)
    digipeater_4 = models.CharField(max_length=9, blank=True)
    digipeater_5 = models.CharField(max_length=9, blank=True)
    digipeater_6 = models.CharField(max_length=9, blank=True)
    digipeater_7 = models.CharField(max_length=9, blank=True)
    information = models.TextField(blank=True)
    hostid = models.IntegerField()
    class Meta:
        db_table = u'raw'
