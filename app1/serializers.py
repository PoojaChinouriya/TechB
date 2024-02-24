from rest_framework import serializers
from .models import TechB


class TechBSerializers(serializers.ModelSerializer):
    class Meta:
        model = TechB
        fields = "__all__"