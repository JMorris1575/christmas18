from django.db import models

class ModelNameMethod(models.Model):

    def get_name(caller, user):
        name = user.first_name
        if name == 'Brian':
            name += ' ' + user.last_name
        return name

    class Meta:
        abstract = True

