from django.db import models
from datetime import datetime, timedelta
import ilmot.custom_fields as custom_fields
from django.core.mail import send_mail
from django.core.exceptions import ValidationError

class StudentGroup(models.Model):
  name = models.CharField(max_length=200)

  def __unicode__(self):
    return self.name

class Cruise(models.Model):
  name = models.CharField(max_length=200)
  registration_start = models.DateTimeField()
  registration_end = models.DateTimeField()

  student_groups = models.ManyToManyField(StudentGroup)

  def __unicode__(self):
    return self.name

class Meal(models.Model):
  name = models.CharField(max_length=200)
  price = models.FloatField()
  cruise = models.ForeignKey(Cruise)

  def __unicode__(self):
    return "{0}, {1}".format(self.name, self.price) 

class Transportation(models.Model):
  legend = models.CharField(max_length=200)
  price = models.FloatField()

  def __unicode__(self):
    return "{0}, {1}".format(self.legend, self.price) 

class CabinCategory(models.Model):
  name = models.CharField(max_length=200)
  capacity = models.IntegerField()
  price = models.FloatField()

  def __unicode__(self):
    return self.name

class Cabin(models.Model):
  #name = models.CharField(max_length=200, blank=True)
  cabin_category = models.ForeignKey(CabinCategory)
  #student_group = models.ForeignKey(StudentGroup)
  cruise = models.ForeignKey(Cruise)

  def capacity(self):
    return self.cabin_category.capacity

  def used(self):
    return self.person_set.count()

  def is_full(self):
    return self.used() >= self.capacity()

  def __unicode__(self):
    return "{0} {1}/{2}".format(self.cabin_category.name, self.used(), self.capacity())

class Person(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  nick_name = custom_fields.CharNullField(max_length=200, unique=True, blank=True, null=True)
  student_group = models.ForeignKey(StudentGroup)
  date_of_birth = models.DateField()
  mail = models.EmailField(max_length=100, unique=True)
  cabin = models.ForeignKey(Cabin, blank=True, null=True)
  transportation = models.ForeignKey(Transportation)
  meals = models.ManyToManyField(Meal)

  access_key = models.CharField(max_length=30, default="", editable=False)
  access_key_expires_at = models.DateTimeField(default=datetime.now, editable=False)

  def clean(self):
    if hasattr(self, 'cabin'):
      if self.cabin == None:
        raise ValidationError("You must select a cabin")
      if self.cabin.is_full() and self not in self.cabin.person_set.all():
        raise ValidationError("The selected cabin is already full, please select another one")
    return super(Person, self).clean()

  def __unicode__(self):
    return self.public_name()

  def public_name(self):
    return self.nick_name if self.nick_name else "{0} {1}".format(self.first_name, self.last_name)

  def _generate_access_key(self, n=8):
    import string
    import random
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(n))

  def set_access_key(self):
    self.access_key = self._generate_access_key()
    expire_datetime = datetime.now() + timedelta(hours=2)
    self.access_key_expires_at = expire_datetime
    self.save()
    sender = "mailbot@ilmot.fi"
    message_body = \
    """Hi {name},
    You can use this key to manage your account on the cruise registration system.
    The key will automatically expire at {expire}.
    Please do not respond to this message.

    Your key is: {key}
    """.format(name=self.first_name, expire=expire_datetime, key=self.access_key)
    send_mail('Your access key for cruise registration system', message_body, sender, [self.mail], fail_silently=False)
