# *-* coding: utf-8 *-*

from django.contrib import admin

from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from threads.models import Thread

#class PersonAdmin(admin.ModelAdmin):
#    pass
#admin.site.register(Person,PersonAdmin)

# subclass AjaxSelectAdmin
class ThreadAdmin(AjaxSelectAdmin):
    # create an ajax form class using the factory function
    #                     model,fieldlist,   [form superclass]
    form = make_ajax_form(Thread,{'participants':'participants'})

admin.site.register(Thread,ThreadAdmin)

