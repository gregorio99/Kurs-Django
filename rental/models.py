from django.db import models
# from django.contrib.auth.models import User
from shelf.models import BookItem
from django.utils.timezone import now

from django.conf import settings


class Rental(models.Model):
    who = models.ForeignKey(settings.AUTH_USER_MODEL)
    # AUTH_USER_MODEL == 'django.contrib.auth.User'
    what = models.ForeignKey(BookItem)
    # when = models.DateTimeField(auto_now_add=True)
    when = models.DateTimeField(default=now)
    returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{who.first_name}".format(who=self.who)
