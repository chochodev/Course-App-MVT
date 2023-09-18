import uuid
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.db import models

class Course(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
  title = models.CharField(verbose_name=(_("Title")), max_length=50, null=True)
  short_description = models.CharField(verbose_name=(_("Short Description")), max_length=100, null=False, blank=False)
  description = models.CharField(verbose_name=(_("Description")), max_length=1000, null=False, blank=False)
  price = models.IntegerField(verbose_name=(_("Price")), null=False, blank=False)
  image = models.ImageField(verbose_name=(_("Course Image")), default='peep-3.jpg', null=False)
  slug = models.SlugField(unique=True, blank=True, null=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
    super().save(*args, **kwargs)

  def __str__(self):
    return f'{self.title[:30]}'

class Video(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
  title = models.CharField(verbose_name=(_("Title")), max_length=50, null=True)
  short_description = models.CharField(verbose_name=(_("Short Description")), max_length=100, null=False, blank=False)
  description = models.CharField(verbose_name=(_("Description")), max_length=1000, null=False, blank=False)
  image = models.ImageField(verbose_name=(_("Course Image")), default='peep-3.jpg', null=False)
  slug = models.SlugField(unique=True, blank=True, null=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
    super().save(*args, **kwargs)
      
  def __str__(self):
    return f'{self.title[:30]}'

class Chat(models.Model):
  pass