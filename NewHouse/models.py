from django.db import models

# Create your models here.
class NewHouse(models.Model):
    community=models.CharField(max_length=50)
    city_area=models.CharField(max_length=10)
    address=models.CharField(max_length=30)
    house_type=models.CharField(max_length=10)
    house_square=models.CharField(max_length=20)
    average_price=models.IntegerField()
    def __str__(self):
        return "community:{} city_area:{} address:{} house_type:{} house_square:{} average_price:{}]".format(self.community,self.city_area,self.address,self.house_type,self.house_square,self.average_price)