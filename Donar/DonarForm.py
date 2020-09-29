from django import forms
from Donar.models import DonarModel

class DonarForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = DonarModel

    b_grops = (('A+','A+'),('B+','B+'),('O+','O+'),('AB+','AB+'),('A-','A-'),('B-','B-'),('O-','O-'),('AB-','AB-'))
    last_donation_date = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    blood_group = forms.ChoiceField(choices=b_grops)
    contact_number_2 = forms.IntegerField(label="Alternate Contact Number")
    email = forms.EmailField()

