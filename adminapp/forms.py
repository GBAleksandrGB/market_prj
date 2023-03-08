from django import forms
from authapp.models import TravelUser
from authapp.forms import TravelUserEditForm
from mainapp.models import ListOfCountries
from mainapp.models import Accommodation


class TravelUserAdminEditForm(TravelUserEditForm):
    """Форма редактирования параметров пользователя"""

    class Meta:
        model = TravelUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control-sm'
            field.help_text = ''


class ListOfCountriesEditForm(forms.ModelForm):
    """Форма редактирования параметров стран"""

    class Meta:
        model = ListOfCountries
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class AccommodationEditForm(forms.ModelForm):
    """Форма редактирования параметров услуг компании"""

    class Meta:
        model = Accommodation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = ''
            field.help_text = ''
