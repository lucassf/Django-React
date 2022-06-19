from rest_framework import serializers
from .models import TradersPnl


class TradersPnlSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradersPnl
        fields = '__all__'
