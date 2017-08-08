from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size':'40','class': 'modal-write__input','placeholder': 'subject'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'size':'40','class': 'modal-write__input'}))
    #message = forms.CharField(widget=forms.Textarea(attrs={'class': 'modal-write__input'}))
    #copy = forms.BooleanField(required=False)

    #widget = forms.TextInput(attrs={'placeholder': 'Search'}))