from rest_framework import serializers
from .models import Member, Trainer, Equipment, Class, Booking, Notification

class MemberSerializer(serializers.ModelSerializer):
  class Meta:
   model = Member
  fields = '__all__'

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
      model = Trainer
     fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
      model = Equipment
    fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
   class Meta:
     model = Class
     fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Booking
   fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
      class Meta:
       model = Notification
      fields = '__all__'