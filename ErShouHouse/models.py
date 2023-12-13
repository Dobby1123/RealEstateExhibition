from django.db import models

# Create your models here.
class ErshouHouse(models.Model):
    introduce=models.CharField(max_length=30)
    house_address=models.CharField(max_length=30)
    house_floor=models.CharField(max_length=10)
    house_square = models.DecimalField(max_digits=5,decimal_places=2)
    ershou_type=models.CharField(max_length=10)
    built_time=models.CharField(max_length=10)
    house_orientations=models.CharField(max_length=5)
    single_price=models.IntegerField()
    total_price=models.IntegerField()
    def __str__(self):
        return "introduce:{} house_address:{} house_floor:{} house_square:{} ershou_type:{} built_time:{} house_orientations:{} single_price:{} total_price:{}]".format(self.introduce,self.house_address,self.house_floor,self.house_square,self.ershou_type,self.built_time,self.house_orientations,self.single_price,self.total_price)