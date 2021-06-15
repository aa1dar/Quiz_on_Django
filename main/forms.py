from .models import Questions
from django import forms

class NameForm(forms.Form):
    CHOICES = [('A', 'A'),('B', 'B'),('C', 'C'),('D', 'D')]
    choice_field1 = forms.ChoiceField(label='',label_suffix='',error_messages='',help_text='',choices=CHOICES,widget=forms.CheckboxSelectMultiple(attrs={
                            'type':'checkbox' ,'value':''}))

