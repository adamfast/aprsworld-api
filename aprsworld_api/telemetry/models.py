from django.db import models

class TelemetryUnits(models.Model):
    source = models.CharField(max_length=10)
    packet_date = models.DateTimeField()
    a_0 = models.TextField()
    a_1 = models.TextField()
    a_2 = models.TextField()
    a_3 = models.TextField()
    a_4 = models.TextField()
    d_0 = models.TextField()
    d_1 = models.TextField()
    d_2 = models.TextField()
    d_3 = models.TextField()
    d_4 = models.TextField()
    d_5 = models.TextField()
    d_6 = models.TextField()
    d_7 = models.TextField()
    class Meta:
        db_table = u'telemetry_units'

class TelemetryLabels(models.Model):
    packet_date = models.DateTimeField()
    source = models.CharField(max_length=10)
    a_0 = models.TextField()
    a_1 = models.TextField()
    a_2 = models.TextField()
    a_3 = models.TextField()
    a_4 = models.TextField()
    d_0 = models.TextField()
    d_1 = models.TextField()
    d_2 = models.TextField()
    d_3 = models.TextField()
    d_4 = models.TextField()
    d_5 = models.TextField()
    d_6 = models.TextField()
    d_7 = models.TextField()
    class Meta:
        db_table = u'telemetry_labels'

class Telemetry(models.Model):
    packet_id = models.IntegerField(primary_key=True)
    source = models.CharField(max_length=10)
    packet_date = models.DateTimeField()
    sequence = models.IntegerField()
    analog_0 = models.IntegerField()
    analog_1 = models.IntegerField()
    analog_2 = models.IntegerField()
    analog_3 = models.IntegerField()
    analog_4 = models.IntegerField()
    digital = models.IntegerField()
    class Meta:
        db_table = u'telemetry'

class TelemetryCoefficients(models.Model):
    source = models.CharField(max_length=10)
    packet_date = models.DateTimeField()
    a_0 = models.FloatField(null=True, blank=True)
    b_0 = models.FloatField(null=True, blank=True)
    c_0 = models.FloatField(null=True, blank=True)
    a_1 = models.FloatField(null=True, blank=True)
    b_1 = models.FloatField(null=True, blank=True)
    c_1 = models.FloatField(null=True, blank=True)
    a_2 = models.FloatField(null=True, blank=True)
    b_2 = models.FloatField(null=True, blank=True)
    c_2 = models.FloatField(null=True, blank=True)
    a_3 = models.FloatField(null=True, blank=True)
    b_3 = models.FloatField(null=True, blank=True)
    c_3 = models.FloatField(null=True, blank=True)
    a_4 = models.FloatField(null=True, blank=True)
    b_4 = models.FloatField(null=True, blank=True)
    c_4 = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'telemetry_coefficients'
