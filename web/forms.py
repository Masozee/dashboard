from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(max_length = 100)
	email = forms.EmailField(max_length = 100)
	subject = forms.CharField(max_length = 150)
	comments = forms.CharField(widget = forms.Textarea, max_length = 2000)