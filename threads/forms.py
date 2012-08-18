# *-* coding: utf-8 *-*

from django import forms

from models import Thread,Message,Group
from tinymce.widgets import TinyMCE
from ajax_select.fields import AutoCompleteSelectMultipleField

class MessageForm(forms.ModelForm):

    class Meta:
        model  = Message
        fields = ['body',]

    def __init__(self, *args, **kwargs):
        """
        Construtor do form de mensagens
        """
        super( MessageForm, self ).__init__(*args, **kwargs)
        self.fields['body'].label = 'Post a message'

    def save(self, thread, user, commit=True):
        instance = super(MessageForm, self).save(commit=False)

        if commit:
            instance.thread = thread
            instance.author = user
            instance.save()

        return instance


class NewThreadForm(forms.ModelForm):

    participants = AutoCompleteSelectMultipleField('participants',help_text=u'')
    body         = forms.CharField('',widget=forms.Textarea)

    class Meta:
        model  = Thread
        fields = ['participants','title','body']

    def save(self, user, commit=True):
        instance = super(NewThreadForm, self).save(commit=False)

        if commit:
            instance.author = user
            instance.save()

            body = self.cleaned_data['body']
            Message.objects.create( thread=instance, author=user, body=body )

        return instance

class NewGroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['name','description','icon','visibility','location']

    def save(self, user, commit=True):
        instance = super(NewGroupForm, self).save(commit=False)

        if commit:
            instance.owner = user
            instance.save()
