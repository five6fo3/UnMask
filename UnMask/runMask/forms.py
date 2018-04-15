from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Twitter username', max_length=100)
