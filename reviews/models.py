from django.db import models

from profiles.models import UserProfile
from products.models import Product


class Review(models.Model):
    """ Class for the Review model """

    class Meta:
        """ Set verbose name """
        verbose_name_plural = 'Reviews'

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Credit Bunny The Compiler
    # https://blog.devgenius.io/lets-build-a-movie-review-django-app-47658f8e3751
    rate_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    stars = models.IntegerField(choices=rate_choices)

    comment = models.TextField(max_length=1500)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.user} | Product: {self.product} | \
                Rating: {self.stars}'
