from rest_framework import serializers
from .models import ProductModel

class PgSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductModel
        fields='__all__'