from django.db import models

class AuthorName(models.Model):

    def get_name(caller=None, user=None):
        name = user.first_name
        if name == 'Brian':
            name += ' ' + user.last_name
        return name

    class Meta:
        abstract = True

