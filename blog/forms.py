from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField()
    message = forms.CharField(required=True, widget=forms.Textarea)



