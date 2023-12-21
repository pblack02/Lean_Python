from django import forms
from django.core import validators


# Create your own validator function
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('Name needs to start with z')


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Verify your email: ')
    text = forms.CharField(widget=forms.Textarea)

    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)])

    # Basic method of validation
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Gotcha bot.")
    #     return botcatcher
    # How to clean the entire form // verify emails
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        vemail = cleaned_data['verify_email']

        if email != vemail:
            raise forms.ValidationError('Emails need to match!')
