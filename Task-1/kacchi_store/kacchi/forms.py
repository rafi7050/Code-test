from django import forms

from .models import kacchi, sells

class kacchiForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(kacchiForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['description'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['price'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }

    class Meta:
        model = kacchi
        fields = ('name', 'description', 'price')


class sellsForm(forms.ModelForm):
     class Meta():
         model = sells
         fields = ('code','kacchi','number_of_plates','date_time','total_price')