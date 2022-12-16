from django import forms
from .widgets import CustomClearableFileInput, CustomClearableFileInputImg
from .models import Ticket, Category


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInputImg)
    countryimg = forms.ImageField(label='Countryimg',
                                  required=False,
                                  widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
