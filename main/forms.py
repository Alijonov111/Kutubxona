from django import forms

from main.models import Muallif, Kitob


class TalabaForm(forms.Form):
    ism = forms.CharField(max_length=255)
    guruh = forms.CharField()
    kurs = forms.IntegerField(min_value=0, max_value=5)
    kitob_soni = forms.IntegerField(min_value=0, max_value=10)


class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = "__all__"


class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = "__all__"
