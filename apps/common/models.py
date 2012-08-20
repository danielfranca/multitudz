from django.db import models
from django.utils.translation import ugettext_lazy as _



class Location(models.Model):

    LOCATION_TYPE = (
        ('CITY','City'),
        ('STATE','State/Province'),
        ('COUNTRY','Country'),
    )

    parent   = models.ForeignKey("Location", related_name="location_parent", verbose_name=_("Parent Location"), null=True)
    location = models.CharField(_('Location'),max_length=100)
    type     = models.CharField(_("Location Type"), choices=LOCATION_TYPE, max_length=100)
