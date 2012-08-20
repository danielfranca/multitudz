# *-* coding: utf-8 *-*

from django.contrib.auth.models import User
from django_facebook import signals
from django_facebook.utils import get_profile_class

def fb_user_registered_handler(sender, user, facebook_data, **kwargs):
    # update user data
    pass

def post_facebook_update(sender, profile, facebook_data, **kwargs):
    # Do other stuff
    import ipdb; ipdb.set_trace()
    pass

profile_class = get_profile_class()

signals.facebook_post_update.connect(post_facebook_update, sender=profile_class)
signals.facebook_user_registered.connect(user_registered, sender=User)

