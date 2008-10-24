from django.db import models

class Message(models.Model):
    packet_id = models.IntegerField(primary_key=True)
    source = models.CharField(max_length=9)
    packet_date = models.DateTimeField()
    addressee = models.CharField(max_length=10, blank=True)
    text = models.CharField(max_length=73, blank=True)
    id = models.CharField(max_length=10, blank=True)
    class Meta:
        db_table = u'messages'
