from django.db import models


# Create your models here.
class AppScrapy(models.Model):
    text = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    class Meta:
        app_label = 'app'
        db_table = 'app_db'


class TuhuTireScrapy(models.Model):
    brand = models.CharField(max_length=255)
    specifications = models.CharField(max_length=255)
    speed_level = models.CharField(max_length=255)
    load_index = models.CharField(max_length=255)
    tire_category = models.CharField(max_length=255)
    tire_pattern = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    evaluate_count = models.CharField(max_length=255)

    class Meta:
        app_label = 'app'
        db_table = 'tuhu_tire_db'


class JingDongScrapy(models.Model):
    brand = models.CharField(max_length=255)
    property = models.CharField(max_length=255)
    commit = models.CharField(max_length=255)
    shop = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

    class Meta:
        app_label = 'app'
        db_table = 'jd_db'


class TmallScrapy(models.Model):
    title = models.CharField(max_length=255)
    shop = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    class Meta:
        app_label = 'app'
        db_table = 'tm_db'


class TuhuScrapy(models.Model):
    displayName = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

    class Meta:
        app_label = 'app'
        db_table = 'th_db'
