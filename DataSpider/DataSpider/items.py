# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy_djangoitem import DjangoItem
from ErShouHouse.models import ErshouHouse
from RentHouse.models import RentHouse
from NewHouse.models import NewHouse

class NewHouseItem(DjangoItem):
    django_model = NewHouse
    pass
class ErShouHouseItem(DjangoItem):
    django_model = ErshouHouse
    pass
class RentHouseItem(DjangoItem):
    django_model = RentHouse
    pass
