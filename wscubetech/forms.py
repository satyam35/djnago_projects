from django import forms

class  userForm(forms.Form):
    num1=forms.CharField(label="val1",required=False)
    num2=forms.CharField(label="val2",required=False)