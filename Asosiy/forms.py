from django import forms
from .models import *


class TalabaForm(forms.Form):
    i = forms.CharField(label="Ism")
    k = forms.IntegerField(label="Kurs")
    k_s = forms.IntegerField(label="Kitoblar soni")


class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = "__all__"


class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = "__all__"

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"

class KutubxonachiForm(forms.ModelForm):
    class Meta:
        model = Kutubxonachi
        fields = "__all__"


