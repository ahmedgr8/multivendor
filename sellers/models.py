from django.conf import settings
from django.db import models
from django.urls import reverse

# Seller account

class SellerAccount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    managers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="manager_sellers",
        blank=True,
        #on_delete=models.CASCADE
    )
    active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return reverse("products:vendor_detail", kwargs={"vendor_name": self.user.username})
