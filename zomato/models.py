from django.db import models
from django.utils.translation import gettext as _


class Restaurant(models.Model):
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=200)
    online_order = models.BooleanField(default=False)
    book_table = models.BooleanField(default=False)
    rate = models.FloatField()
    votes = models.IntegerField()
    location = models.CharField(max_length=200)
    rest_type = models.CharField(max_length=200)
    cuisines = models.CharField(max_length=200)
    cost2plates = models.FloatField()
    listed_in_type = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    ratings = models.CharField(max_length=600)
    reviews = models.CharField(max_length=1000)
    count = models.IntegerField()
    sentiments = models.CharField(max_length=200)
    summaries = models.CharField(max_length=200)
    sentiment_label = models.CharField(max_length=200)
    index_f = models.IntegerField()

    def __str__(self):
        return self.name