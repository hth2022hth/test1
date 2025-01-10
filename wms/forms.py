from django import forms
from .models import Warehouse


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['name']
        labels = {
            'name': '仓库名称',
        }


def clean_name(self):
    name = self.cleaned_data.get('name')
    name = name.strip
    if Warehouse.objects.filter(name=name).exists():
        raise forms.ValidationError('仓库名称已存在。')
    return name
