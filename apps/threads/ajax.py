# *-* coding: utf-8 *-*

from dajax.core.Dajax import Dajax
from dajaxice.decorators import dajaxice_register
from django.template.loader import render_to_string

from threads.models import Message, Thread
from threads.forms import MessageForm

import logging

@dajaxice_register
def refresh_messages(request, thread_id):
    dajax = Dajax()

    from expow.settings import STATIC_URL

    html_string = ''
    for message in Message.objects.filter( thread__id=thread_id ):
        html_string += render_to_string('threads/thread_message.html',{'message':message,'STATIC_URL':STATIC_URL})

    dajax.assign('#thread-messages','innerHTML',html_string)

    return dajax.json()

@dajaxice_register
def send_reply(request=None, thread_id=None, form=None):

    form = MessageForm(form)

    if form.is_valid():
        form.save(Thread.objects.get(id=thread_id), request.user)
        return refresh_messages(request, thread_id)

    return Dajax().json()



