from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.contrib import messages
from .models import Approval
from .form import ApprovalForm
from .serializers import ApprovalSerializers
# from keras.models import load_model
import joblib
import numpy as np
import pandas as pd
from sklearn import preprocessing
import json
# from keras import backend as K

# Create your views here.

import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=UserWarning)

class ApprovalView(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializers

def mapdata(df):
    ohe_col = joblib.load('django-loan1\static\all_col.sav')
    cat_columns = ['Gender','Married', 'Education', 'Self_Employed', 'Property_Area']
    df1=pd.get_dummies(df, columns=cat_columns)
    newdf = {}
    for i in ohe_col:
        if i in df1.columns:
            newdf[i]= df1[i].values
        else:
            newdf[i] = 0
    newdf1 = pd.DataFrame(newdf)
    return newdf1

# def mapdata(df):
#     map_col1={'No':1,'Yes':2}
#     df['Self_Employed']=df['Self_Employed'].map(map_col1)
#     # map_col2={'0':1,'1':2, '2':3, '3+':4}
#     # df['Dependents']=df['Dependents'].map(map_col2)
#     map_col3={'Urban':1,'Rural':2, 'Semiurban':3}
#     df['Property_Area']=df['Property_Area'].map(map_col3)
#     map_col4={'Graduate':1,'Not Graduate':2}
#     df['Education']=df['Education'].map(map_col4)
#     map_col5={'No':1,'Yes':2}
#     df['Married']=df['Married'].map(map_col5)
#     map_col6={'Male':1,'Female':2}
#     df['Gender']=df['Gender'].map(map_col6)
#     return df

# def mapdata(df):
#     cat_columns = ['Gender','Married', 'Education', 'Self_Employed', 'Property_Area']
#     for col in cat_columns:
#         if(df[col])

# @api_view(["POST"])
# def ApprovalReject(request):
#     try:
#         model = joblib.load('C:/Users/George D/Visual Studio/Django/django-loan/static/simple_model1.sav')
#         mydata = request.data
#         unit = np.array(list(mydata.values()))
#         unit = unit.reshape(1,-1)
#         scalers = joblib.load('C:/Users/George D/Visual Studio/Django/django-loan/static/scaler.sav')
#         X = scalers.transform(unit)
#         y_pred = model.predict(X)
#         y_pred = (y_pred>0.55)
#         newdf = pd.DataFrame(y_pred, columns=['Status'])
#         newdf = newdf.replace({True:'Approved', False:'Rejected'})
#         return JsonResponse('Your Status is {}'.format(newdf), safe=False)
#     except ValueError as e:
#         return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

# @api_view(["POST"])
def ApprovalReject(unit):
    try:
        model = joblib.load('django-loan1\static\gradient_model.sav')
        # mydata = request.data
        # unit = np.array(list(mydata.values()))
        # unit = unit.reshape(1,-1)
        scalers = joblib.load('django-loan1\static\scaler.sav')
        X = scalers.transform(unit)
        y_pred = model.predict(X)
        # y_pred = (y_pred<1)
        newdf = pd.DataFrame(y_pred, columns=['Status'])
        newdf = newdf.replace({1:'Approved', 2:'Rejected'})
        return ('Your Status is {}'.format(newdf.values[0][0]))
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def CxContact(request):
    if request.method=='POST':
        form=ApprovalForm(request.POST)
        if form.is_valid():
            # Firstname=form.cleaned_data['Firstname']
            # Lastname=form.cleaned_data['Lastname']
            Gender=form.cleaned_data['Gender']
            Married =form.cleaned_data['Married']
            # Dependents = form.cleaned_data['Dependents']
            Education = form.cleaned_data['Education']
            Self_Employed = form.cleaned_data['Self_Employed']
            ApplicantIncome = form.cleaned_data['ApplicantIncome']
            CoapplicantIncome = form.cleaned_data['CoapplicantIncome']
            LoanAmount  = form.cleaned_data['LoanAmount']
            Loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
            Credit_History = form.cleaned_data['Credit_History']
            Property_Area = form.cleaned_data['Property_Area']
            mydict = (request.POST).dict()
            df=pd.DataFrame(mydict, index=[0])
            print(mapdata(df))
            
            print(ApprovalReject(mapdata(df)))
            answer = ApprovalReject(mapdata(df))
            messages.success(request, 'Application Status: {}'.format(answer))

    form = ApprovalForm()
    return render(request,'myform/cxform.html', {'form':form})