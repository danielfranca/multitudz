# *-* coding: utf-8 *-*

from django.shortcuts import Http404, render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from models import Thread,Message
from forms import MessageForm,NewThreadForm,NewGroupForm

def show_thread(request, thread_id):

    """
    Mostra a thread com base no seu thread_id
    @param request:
    @param thread_id:
    @return:
    @raise:
    """
    try:
        thread = Thread.objects.get(id=thread_id)
    except Thread.DoesNotExist:
        raise Http404

    message_form = MessageForm(request.POST or None)
    if message_form.is_valid():
        message_form.save(thread,request.user)

    messages = Message.objects.filter(thread=thread)

    return render_to_response(
        'threads/thread.html',
        {
            'thread':thread,
            'message_form': MessageForm(),
            'messages': messages,
        },
        context_instance=RequestContext(request)
    )


@login_required
def new_thread(request):

    """
    Cria uma nova thread

    @param request:
    @return:
    """
    new_thread_form = NewThreadForm(request.POST or None)
    if new_thread_form.is_valid():
        thread = new_thread_form.save(request.user)
        return redirect( reverse( 'show_thread', args=(thread.id,) ) )

    return render_to_response(
        'threads/new_thread.html',
        {
            'new_thread_form': new_thread_form,
        },
        context_instance=RequestContext(request)
    )

@login_required
def new_group(request):

    """
    Cria um novo grupo

    @param request:
    @return:
    """
    new_group_form = NewGroupForm(request.POST or None)
    if new_group_form.is_valid():
        group = new_group_form.save(request.user)
        #FIXME: Redirecionar pra onde mostra o grupo
        #return redirect( reverse( 'show_thread', args=(thread.id,) ) )

    return render_to_response(
        'threads/new_group.html',
            {
            'new_group_form': new_group_form,
            },
        context_instance=RequestContext(request)
    )

def search_groups(request):
    pass
