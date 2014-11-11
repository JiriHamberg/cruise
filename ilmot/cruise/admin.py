from django.contrib import admin
from cruise.models import Cruise, StudentGroup, Meal, Cabin, CabinCategory, Person, Transportation
# Register your models here.

admin.site.register(Cruise)
admin.site.register(StudentGroup)
admin.site.register(Meal)
admin.site.register(Cabin)
admin.site.register(CabinCategory)
admin.site.register(Person)
admin.site.register(Transportation)