# serializers.py
from rest_framework import serializers
from .models import Cards

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ['id', 'title', 'description', 'column']
   

    def validate_description(self, value):
        if len(value) < 25:
            raise serializers.ValidationError("Description should be a minimum of 25 characters.")
        return value
    
