from django.forms import ModelForm

from security.models import Contact

class ContactForm(ModelForm):
    
    class Meta:
        model = Contact
        fields = ("full_name", "email", "subject", "message", )
