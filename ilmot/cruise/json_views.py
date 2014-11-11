#from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from cruise.models import Cabin, Person


def cabin_categories(request):
	cabin_categories = {'All': []}
	def first_person_student_group(cabin):
		if len(cabin.person_set.all()) > 0:
			return cabin.person_set.all()[0].student_group.name
		else:
			return 'Empty'
	for cabin in Cabin.objects.all():
		cabin_categories['All'].append(cabin.id)
		key = first_person_student_group(cabin)
		if key in cabin_categories:
			cabin_categories[key].append(cabin.id)
		else:
			cabin_categories[key] = [cabin.id]
	return JsonResponse(cabin_categories)

def person_info(request):
	persons = {}
	for person in Person.objects.all():
		info = {
			'public_name': str(person),
			'group': person.student_group.name
		}
		persons[person.id] = info
	return JsonResponse(persons) 