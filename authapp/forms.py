from django import forms
from django.contrib.auth.forms import AuthenticationForm, \
    UserChangeForm, UserCreationForm

from .models import TravelUser, TravelUserProfile


class TravelUserRegisterForm(UserCreationForm):
    """Форма регистрации пользователя"""

    class Meta:
        model = TravelUser
        fields = ('username', 'first_name', 'password1',
                  'password2', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data


class TravelUserEditForm(UserChangeForm):
    """Форма редактирования регистрационных данных пользователя"""

    class Meta:
        model = TravelUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar',
                  'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("ВЫ слишком молоды!")

        return data


class TravelUserLoginForm(AuthenticationForm):
    """Форма для аутентификации"""

    class Meta:
        model = TravelUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(TravelUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class TravelUserProfileEditForm(forms.ModelForm):
    """Форма для редактирования профиля пользователя"""

    class Meta:
        model = TravelUserProfile
        fields = ('tagline', 'aboutMe', 'gender')

    def __init__(self, *args, **kwargs):
        super(TravelUserProfileEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
