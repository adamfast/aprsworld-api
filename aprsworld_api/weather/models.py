from django.db import models

class LastWeather(models.Model):
    packet_id = models.IntegerField(primary_key=True)
    source = models.CharField(max_length=9, primary_key=True)
    packet_date = models.DateTimeField()
    wind_direction = models.IntegerField(null=True, blank=True)
    wind_speed = models.IntegerField(null=True, blank=True)
    wind_gust = models.IntegerField(null=True, blank=True)
    wind_sustained = models.IntegerField(null=True, blank=True)
    temperature = models.IntegerField(null=True, blank=True)
    rain_hour = models.FloatField(null=True, blank=True)
    rain_calendar_day = models.FloatField(null=True, blank=True)
    rain_24hour_day = models.FloatField(null=True, blank=True)
    humidity = models.IntegerField(null=True, blank=True)
    barometer = models.FloatField(null=True, blank=True)
    luminosity = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'lastweather'

class Weather(models.Model):
    packet_id = models.IntegerField(primary_key=True)
    source = models.CharField(max_length=9)
    packet_date = models.DateTimeField()
    wind_direction = models.IntegerField(null=True, blank=True)
    wind_speed = models.FloatField(null=True, blank=True)
    wind_gust = models.FloatField(null=True, blank=True)
    wind_sustained = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    rain_hour = models.FloatField(null=True, blank=True)
    rain_calendar_day = models.FloatField(null=True, blank=True)
    rain_24hour_day = models.FloatField(null=True, blank=True)
    humidity = models.IntegerField(null=True, blank=True)
    barometer = models.FloatField(null=True, blank=True)
    luminosity = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'weather'
