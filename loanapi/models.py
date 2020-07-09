from django.db import models

# Create your models here.
class Approval(models.Model):

    gender_choice = (
        ('Male','Male'),
        ('Female','Female'),
    )

    married_choice =(
        ('Yes','Yes'),
        ('Yes','Yes'),
    )

    education_choice = (
        ('Graduate','Graduate'),
        ('Not_Graduate','Not_Graduate'),
    )

    area_choice = (
        ('Urban','Urban'),
        ('Rural','Rural'),
        ('Semiurban','Semiurban')
    )

    employed_choice = (
        ('Yes','Yes'),
        ('No', 'No')
    )

    # firstname=models.CharField(max_length=100)
    # lastname=models.CharField(max_length=100, help_text='Please enter your Surname here')
    gender=models.CharField(max_length=10,null=True, choices=gender_choice,help_text='Please select male or female')
    married =models.CharField(max_length=4, null=True,choices=married_choice)
    # dependents = models.IntegerField(default=0)
    education = models.CharField(max_length=100, choices=education_choice, help_text='Please indicate if you are a graduate or not', null=True)
    self_employed = models.CharField(max_length=5, choices=employed_choice,help_text="Please indicate with a 'Yes' or 'No'", null=True)
    applicant_income = models.IntegerField(default=0)
    coapplicant_income = models.IntegerField(default=0)
    loan_amount  = models.IntegerField(default=0)
    loan_amount_term = models.IntegerField(default=0)
    credit_history = models.IntegerField(default=0)
    property_area = models.CharField(max_length=15, choices=area_choice, null=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
