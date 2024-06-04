from django.forms import ModelForm

from security.models import Contact, Subscribe

class ContactForm(ModelForm):
    
    class Meta:
        model = Contact
        fields = ("full_name", "email", "subject", "message", )



class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ('email',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email'})
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})