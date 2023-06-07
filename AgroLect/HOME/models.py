from pyexpat import model
from django.db import models

# Create your models here.


#General Data
class Crop(models.Model):
    Crop_name= models.CharField(max_length=255)
    avg_humidity = models.FloatField()
    avg_ph,avg_temp =models.FloatField(), models.FloatField()

class Location(models.Model):
    Location = models.CharField(max_length=255)
    max_humidity = models.FloatField()
    min_humidity = models.FloatField()
    max_ph,max_temp =models.FloatField(), models.FloatField()
    min_ph,min_temp =models.FloatField(), models.FloatField()
    avg_temp,avg_ph,avg_humidity = models.FloatField(), models.FloatField(),models.FloatField()

class Userdata(models.Model):
    user_name = models.CharField(max_length=255)
    Location = models.CharField(max_length=255)
    Crop_name= models.CharField(max_length=255)
    max_humidity = models.FloatField()
    min_humidity = models.FloatField()
    max_ph,max_temp =models.FloatField(), models.FloatField()
    min_ph,min_temp =models.FloatField(), models.FloatField()
    avg_humidity = models.FloatField()
    avg_ph,avg_temp =models.FloatField(), models.FloatField()
    price = models.FloatField()

class MAP(models.Model):
    CONTINENTS = (
        ('NA', 'North America'),
        ('AS', 'Asia'),
    )
    RegionName = models.CharField(max_length=200, choices=CONTINENTS)
    Countries = (
        ('CA', 'Canada'),
        ('MX', 'Mexico'),
        ('US', 'United States'),
        ('RU', 'Russia'),
        ('IND', 'India'),
        ('CH', 'China'),
    )
    country = models.CharField(max_length=20, choices=Countries)
    Cities = (
        ('ON', 'Ontario'), ('AB', 'Alberta'), ('TO', 'Toronto'), ('QB',
                                                                  'Quebec'), ('SN', 'Sinaloa'), ('BC', 'Baja California'),
        ('OZ', 'Orizabo'), ('CH', 'Chihuahua'), ('OA', 'Oaxaca'), ('AK',
                                                                   'Arkansas'), ('WN', 'Washington'), ('GRG', 'Georgia'), ('TXS', 'Texas'),
        ('IW', 'Iowa'), ('KR', 'Krasnodar'), ('RT', 'Rostov'), ('ST',
                                                                'Stavropol'), ('SB', 'Siberia'), ('FZ', 'Faizabad'), ('AM', 'Amritsar'),
        ('KTK', 'Kolkata'), ('AMD', 'Ahmedabad'), ('CHW', 'Chhindwara'), ('GZ',
                                                                          'Guizhou'), ('GDG', 'Guangdong'), ('XNG', 'Xinjiang'), ('UQI', 'Urumqi'),
    )
    cities = models.CharField(max_length=20, choices=Cities)
    