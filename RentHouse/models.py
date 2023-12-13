from django.db import models

# Create your models here.
class RentHouse(models.Model):
    rent_introduce=models.CharField(max_length=50)
    rent_address=models.CharField(max_length=50)
    rent_style=models.CharField(max_length=10)
    rent_square=models.DecimalField(max_digits=5,decimal_places=2)
    rent_orientations=models.CharField(max_length=5)
    month_price=models.IntegerField()
    def __str__(self):
        return "rent_introduce:{} rent_address:{} rent_style:{} rent_square:{} rent_orientations:{} month_price:{}]".format(self.rent_introduce,self.rent_address,self.rent_style,self.rent_square,self.rent_orientations,self.month_price)