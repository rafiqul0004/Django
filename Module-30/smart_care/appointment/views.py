from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
  
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer

    def get_queryset(self):
        queryset=super().get_queryset() #main query set ke inherit korlam

        patient_id=self.request.query_params.get('patient_id') #param theke patient id nilam

        if patient_id:
            queryset=queryset.filter(patient_id=patient_id) #filter by patient_id
        return queryset

