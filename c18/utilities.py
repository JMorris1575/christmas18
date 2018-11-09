def get_name(user):
    name = user.first_name
    if name == 'Brian':
        name += ' ' + user.last_name
    return name