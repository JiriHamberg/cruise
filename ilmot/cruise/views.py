from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from datetime import datetime
from django.utils import timezone
from django.contrib import messages
from django.db import transaction


from cruise.models import Cabin, Person
from cruise.forms import PersonAuthenticationKeyForm, PersonAuthenticationMailForm
from cruise.authentication import person_authenticate, person_invalidate_access_key

def index(request):
  return HttpResponse("Hello, this is index")

class CabinView(generic.ListView):
  template_name = 'cruise/cabin/list.html'
  context_object_name = 'cabins'

  def get_queryset(self):
    return Cabin.objects.all()

class PersonRegister(CreateView):
  model = Person
  success_url = "cruise/person/edit"

  def get_context_data(self, **kwargs):
  	data = super(PersonRegister, self).get_context_data(**kwargs)
  	data['cabins'] = Cabin.objects.all()
  	return data

  @transaction.atomic
  def form_valid(self, form):
	messages.success(self.request, "Your registration was succesful")
	return super(PersonRegister, self).form_valid(form)

class PersonUpdate(UpdateView):
  model = Person
  success_url = "/cruise/person/edit"

  @transaction.atomic
  def form_valid(self, form):
  	"invalidate access key and post changes"
  	if not person_authenticate(self.request.session['access_key'], self.object):
  		raise PermissionDenied()
  	cabin = self.object.cabin
  	res = super(PersonUpdate, self).form_valid(form)
  	person_invalidate_access_key(self.object)
  	messages.success(self.request, "Your registration was updated")
  	return res

  def get_context_data(self, **kwargs):
  	data = super(PersonUpdate, self).get_context_data(**kwargs)
  	data['cabins'] = Cabin.objects.all()
  	return data

  def get_object(self):
  	"get object if we have a valid access key in session"
  	object = super(PersonUpdate, self).get_object()
  	if person_authenticate(self.request.session.get('access_key'), object):
  		return object
  	else:
  		raise PermissionDenied()

class PersonAuthenticate(generic.TemplateView):
	template_name = "cruise/person_authenticate.html"
	
	def get_context_data(self, **kwargs):
		context = super(PersonAuthenticate, self).get_context_data(**kwargs)
		context['key_form'] = PersonAuthenticationKeyForm()
		context['mail_form'] = PersonAuthenticationMailForm()
		return context
	
	def post(self, request, **kwargs):
		if 'mail' in request.POST: #generate new access key and send it via mail
			mail = request.POST['mail']
			persons = Person.objects.filter(mail = mail)
			if len(persons) == 1:
				self.request.session['mail'] = mail
				persons[0].set_access_key()
				messages.success(request, "Access key was sent to {}".format(mail))
			else:
				messages.error(request, 'No registration with mail {}'.format(mail))
			return HttpResponseRedirect('/cruise/person/edit')

		elif 'key' in request.POST: #authenticate user by access key
			key = request.POST['key']
			if 'mail' not in request.session:
				messages.error(request, 'No access key has been sent to you yet. Please give a valid mail address.')
				return HttpResponseRedirect('/cruise/person/edit')
			mail = request.session['mail']
			persons = Person.objects.filter(access_key = key, mail = mail)
			if len(persons) == 1:
				self.request.session['access_key'] = key
				return HttpResponseRedirect('/cruise/person/{id}'.format(id=persons[0].id))
			else:
				messages.error(request, 'Invalid access key')
				return HttpResponseRedirect('/cruise/person/edit')
		raise Http400()