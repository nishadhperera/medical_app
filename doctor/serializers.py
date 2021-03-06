from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ('name',
                  'age',
                  'reg_id',
                  'date_of_birth',
                  'email',
                  'address',
                  'mobile_number',
                  'specialization',
                  )
