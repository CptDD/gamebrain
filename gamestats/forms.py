from django import forms
from django.contrib.auth.models import User

import logging


logger = logging.getLogger(__name__)

class ContactForm(forms.Form):
	
	name = forms.CharField(label='Name', max_length=100)
	message = forms.CharField(max_length=600,widget=forms.Textarea)
	
	
	def send(self):
		print('We are her to make some noise!')
	

class UserForm(forms.ModelForm):
	
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model=User
		fields=('username','password')


