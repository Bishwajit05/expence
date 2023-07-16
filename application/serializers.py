from rest_framework import serializers
from .models import *


class TrackerSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="Enter expense Id")
    buy = serializers.CharField(label="Enter cost")
    reason = serializers.CharField(label="Enter reason")


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = accounts
        fields = "__all__"
