from rest_framework import serializers
from django.db.models import Avg,Sum
from .models import Table

# Create your serializers here.
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'email', 'name','phone']
        