from django import forms
from appTwo.models import User


class UserForm(forms.ModelForm):
    # Validations would go here.
    class Meta:
        model = User
        fields = '__all__'
