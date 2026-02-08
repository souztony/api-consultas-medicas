from rest_framework import serializers
from .models import Appointment
from apps.professionals.serializers import ProfessionalSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    professional_detail = ProfessionalSerializer(source='professional', read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'date', 'professional', 'professional_detail', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
