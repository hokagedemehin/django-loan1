from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
urlpatterns = [
    # path('form/', views.myform, name='myform'),
    path('api/', include(router.urls)),
    path('status/', views.ApprovalReject, name='approval'),
    path('', views.CxContact, name='cxform')
]
