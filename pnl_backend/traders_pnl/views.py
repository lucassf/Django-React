from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TradersPnlSerializer
from .models import TradersPnl


class PnlTradersView(viewsets.ModelViewSet):
    serializer_class = TradersPnlSerializer
    queryset = TradersPnl.objects.all()
