from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    product_category = models.CharField(max_length=50, default="")
    product_name = models.CharField(max_length=100, default="")
    display_image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_category




