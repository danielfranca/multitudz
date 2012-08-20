# *-* coding: utf-8 *-*

from ajax_select import LookupChannel
from django.utils.html import escape
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from expow.settings import STATIC_URL

#from django.contrib.auth.models import Group
from threads.models import Group

class ParticipantLookup(LookupChannel):

    model = User

    def get_query(self,q,request):
        result  = list( User.objects.filter(Q(username__icontains=q) | Q(email__istartswith=q) | Q(first_name__icontains=q) | Q(last_name__icontains=q) ).order_by('username') )
        result += list( Group.objects.filter( Q(name__icontains=q)|Q(description__icontains=q) ).order_by('name') )

        return result

    def get_result(self,obj):
        u""" result is the simple text that is the completion of what the person typed """
        if isinstance(obj,User):
            return obj.username
        else:
            return obj.name


    def format_match(self,obj):
        """ (HTML) formatted item for display in the dropdown """
        return self.format_item_display(obj)

    def format_item_display(self,obj):
        """ (HTML) formatted item for displaying item in the selected deck area """
        from easy_thumbnails.files import get_thumbnailer
        if isinstance(obj, User):
            try:
                profile = obj.get_profile()
                thumb_url = get_thumbnailer(profile.image)['avatar_20'].url
                return u"<div>%s</div><img src='%s'')/>" % (escape(obj.first_name+' '+obj.last_name),STATIC_URL+str(thumb_url))
            except:
                return u"%s" % (escape(obj.username))
        else:
            return u"<div>%s</div><img />" % (escape(obj.name),STATIC_URL+str(obj.icon))

    def check_auth(self, request):
        if not request.user.is_authenticated:
            raise HttpResponseForbidden('Who are you?')




