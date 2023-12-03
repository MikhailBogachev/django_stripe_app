from django.db import models


class Item(models.Model):
    RUBLES = "rub"
    DOLLARS = "usd"
    CURRENCY_IN_ITEM_CHOICES = [
        (RUBLES, "Rubles"),
        (DOLLARS, "Dollars"),
    ]
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_IN_ITEM_CHOICES,
        default=DOLLARS,
    )

    def __str__(self):
        return self.name
