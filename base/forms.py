from django import forms
from .models import ContactProfile


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			'class': 'contact__input'
			}))
    subject = forms.CharField(max_length=200, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Subject..',
			'class': 'contact__input'
			}))
    email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Email..',
			'class': 'contact__input'
			}))
    message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': '*Message..',
			'class': 'contact__input',
			'rows': 6,
			}))
    class Meta:
        model = ContactProfile
        fields = ('name', 'subject', 'email', 'message')