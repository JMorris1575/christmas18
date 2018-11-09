from gift.models import Gift


def user_has_gift(user):            # to be used in views to create a context variable for templates to use
    return len(Gift.objects.filter(receiver=user)) != 0