from rest_framework import serializers
from .models import Approval

class ApprovalSerializers(serializers.ModelSerializer):
    class Meta:
        model=Approval
        fields= '__all__'