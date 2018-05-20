from django.db import models
from django.core.exceptions import ValidationError

class Price(models.Model):
    product_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=True)
    store = models.CharField(max_length=50)
    location = models.CharField(max_length=50)    # local
    url = models.URLField()    # online

    def __repr__(self):
        return ("<Price(id={}, name={}, price={}, unit={}, record_time={})>"
               .format(self.id, self.name, self.price, self.unit, self.time))

    def clean(self):
        if (not self.location) and (not self.url):
            raise ValidationError("location and url can't be both blank.")

