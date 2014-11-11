from cruise.models import Cabin, Person
from django.utils import timezone
from datetime import datetime

def person_authenticate(access_key, person):
	time_now = timezone.make_aware(datetime.now(), timezone.get_default_timezone())
  	return person.access_key_expires_at > time_now and access_key == person.access_key

def person_invalidate_access_key(person):
	person.access_key_expires_at = timezone.make_aware(datetime.now(), timezone.get_default_timezone())
  	person.save()
