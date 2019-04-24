from django.db import models
from datetime import datetime

# Expanding the core model to give us more to work with
### realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
# ^ linking that field to the ID of the realtor
#   second param is what to do with *this* record if the
#   associated foreign record is deleted (want to keep, delete it, etc.)
### title = models.CharField(max_length=200)
# ^ set it to a character field with max length of 200 char
### description = models.TextField(blank=True)
# ^ setting blank=True makes the field optional


class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
        # for admin area, this is the main field to be displayed
