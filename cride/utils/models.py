"""Djando models utilities."""

# Django
from django.db import models

class CRideModel(models.Model):
  """Comparte ride base model

  CRideModel acts as an abstract base class from wich every 
  other model in the project will inherit. This class provides
  every table with the following attributes:
    + created (Datetime): Store the datetime the object was created.
    + modified (Datetime): Store the last datetime the object was modified.
  """
  created = models.DatetimeField(
    'created_at',
    auto_now_add=True,
    help_text='Date time on which the object was created'
  )
  modified = models.DatetimeField(
    'modified_at',
    auto_now=True,
    help_text='Date time on which the object was last modified'
  )

  class Meta:
    """Meta option."""
    abstract = True
    get_latest_by = 'created'
    ordering = ['-created','-modified']
