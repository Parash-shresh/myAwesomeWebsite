from email.mime import image
from django.db import models

# Create your models here.

# yo Product model lai admin.py ma register garna parxa jun gari sakyo
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()

    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to = "shop/images", default = "")

    #yahi class Product vitra yo __str__(self) vanne method banako. admin panel ma productobject ko satta product name display garna lai
    def __str__(self) :
        return self.product_name