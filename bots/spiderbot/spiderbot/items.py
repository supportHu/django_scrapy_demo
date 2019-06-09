# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from app.models import AppScrapy
from app.models import TuhuTireScrapy
from app.models import JingDongScrapy
from app.models import TmallScrapy
from app.models import TuhuScrapy


class SpiderbotItem(DjangoItem):
    django_model = AppScrapy


class TuhuTireItem(DjangoItem):
    django_model = TuhuTireScrapy


class JingDongItem(DjangoItem):
    django_model = JingDongScrapy


class TmallItem(DjangoItem):
    django_model = TmallScrapy


class TuhuItem(DjangoItem):
    django_model = TuhuScrapy

