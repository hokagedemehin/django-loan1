from django.forms import ModelForm
from django import forms

class ApprovalForm(forms.Form):
    # Firstname=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Enter FIrst Name Here'}))
    # Lastname=forms.CharField(max_length=100, help_text='Please enter your Surname here')
    Gender=forms.ChoiceField(choices=[('Male','Male'),('Female','Female')])
    Married =forms.ChoiceField(choices=[('Yes','Yes'),('No','No')])
    # Dependents = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter number of descendant here'}))
    Education = forms.ChoiceField(choices=[('Graduate','Graduate'),('Not_Graduate','Not_Graduate')])
    Self_Employed = forms.ChoiceField(choices=[('Yes','Yes'),('No','No')],help_text="Please indicate with a 'Yes' or 'No'")
    ApplicantIncome = forms.IntegerField()
    CoapplicantIncome = forms.IntegerField()
    LoanAmount  = forms.IntegerField()
    Loan_Amount_Term = forms.IntegerField()
    Credit_History = forms.IntegerField()
    Property_Area = forms.ChoiceField(choices=[('Rural','Rural'),('Urban','Urban'),('Semiurban','Semiurban')])