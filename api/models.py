from django.db import models
from api.fields import JSONField
# Create your models here.
class Category(models.Model):
    title = models.TextField()

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.TextField()
    description = models.TextField()
    filename = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
class Sale(models.Model):
    name = models.TextField()
    address1 = models.TextField()
    address2 = models.TextField(null=True, blank=True)
    city = models.TextField()
    state = models.TextField()
    zipcode = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    items = JSONField(default=dict)
    payment_intent = JSONField(default=dict)

class AppStore(models.Model):
    track_name = models.TextField(null=True, blank=True)
    size_bytes = models.TextField(null=True, blank=True)
    currency = models.TextField(null=True, blank=True)
    price = models.TextField(null=True, blank=True)
    rating_count_tot = models.TextField(null=True, blank=True)
    rating_count_ver = models.TextField(null=True, blank=True)
    user_rating = models.TextField(null=True, blank=True)
    user_rating_ver = models.TextField(null=True, blank=True)
    ver = models.TextField(null=True, blank=True)
    cont_rating = models.TextField(null=True, blank=True)
    prime_genre = models.TextField(null=True, blank=True)
    sup_devices_num = models.TextField(null=True, blank=True)
    ipadSc_urls_num = models.TextField(null=True, blank=True)
    lang_num = models.TextField(null=True, blank=True)
    vpp_lic = models.TextField(null=True, blank=True)
    app_desc = models.TextField(null=True, blank=True)
    
    