from django import forms

class ContactForm(forms.Form):
	name = forms.CharField()
	age = forms.CharField()
	phone = forms.CharField()
	email = forms.CharField()