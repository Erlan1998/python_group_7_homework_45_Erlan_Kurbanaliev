from django import forms
from django.forms import widgets
from webapp.models import status_choices



class ListForm(forms.Form):
    """
    Форма для создания и редактирваония объектов статьи
    https://docs.djangoproject.com/en/3.1/ref/forms/
    """
    description = forms.CharField(max_length=200,  required=True, label='Здача')
    detailed_description = forms.CharField(max_length=3000, widget=widgets.Textarea, label='Подробная Информация')
    status = forms.ChoiceField(required=True, choices=status_choices, label='Статус')
    updated_at = forms.DateField(label='Дата завершеня!')