from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from common.models import Location

class Group(models.Model):

    VISIBILITY = (
        ('PR','Private (Only members)'),
        ('PU','Public (Everyone)'),
    )

    name          = models.CharField(_('Name'), max_length=255)
    description   = models.TextField(_('Description'), max_length=1024)
    icon          = models.ImageField(_('Icon'),upload_to='.',null=True, blank=True)
    owner         = models.ForeignKey(User, related_name='group_owner')
    visibility    = models.CharField(_('Visibility'), choices=VISIBILITY, max_length=50)
    moderators    = models.ManyToManyField(User, related_name='group_moderators', null=True)
    location      = models.ForeignKey(Location,related_name='group_location', null=True, blank=True)
    members       = models.ManyToManyField(User, related_name='group_members')
    banned_users  = models.ManyToManyField(User, related_name='group_banned_members', null=True)
    creation_time = models.DateTimeField(_('Creation Time'), auto_now_add=True)


class Thread(models.Model):

    title        = models.CharField(_('Title'), max_length=255)
    start_date   = models.DateTimeField(_('Start Date'), auto_now_add=True)
    participants = models.ManyToManyField(User, related_name='thread_participants')
    author       = models.ForeignKey(User, related_name='thread_author')

class Message(models.Model):

    thread       = models.ForeignKey(Thread, related_name='message_thread')
    body         = models.TextField(_('Body'),  max_length=4096)
    post_date    = models.DateTimeField(_('Post Date'), auto_now_add=True)
    last_edited  = models.DateTimeField(_('Last Edited'), auto_now=True)
    author       = models.ForeignKey(User, related_name='message_author')

class Inbox(models.Model):

    user         = models.ForeignKey(User, related_name='inbox_user')
    threads      = models.ManyToManyField(Thread,related_name='inbox_threads')


class Entity(models.Model):

    ENTITY_TYPE = (
        ('USER','User'),
        ('GROUP','Group'),
    )

    type         = models.CharField(_('Entity Type'), choices=ENTITY_TYPE, max_length=50)
    user         = models.ForeignKey(User, related_name='entity_user')
    group        = models.ForeignKey(Group, related_name='entity_group')