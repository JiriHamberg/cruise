from django import forms

class PersonAuthenticationKeyForm(forms.Form):
	key = forms.CharField(initial='Your authentication token')

class PersonAuthenticationMailForm(forms.Form):
	mail = forms.EmailField()