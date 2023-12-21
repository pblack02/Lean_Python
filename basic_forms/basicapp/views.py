from django.shortcuts import render
from basicapp import forms


# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')


def form_name_view(request):
    form = forms.FormName()

    # How to grad data from the post request
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # Do something code
            print('Validation Successful')
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form': form})
