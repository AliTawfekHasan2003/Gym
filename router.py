from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MemberViewSet, TrainerViewSet, EquipmentViewSet,
    ClassViewSet, BookingViewSet, NotificationViewSet
)

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'trainers', TrainerViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('api', include(router.urls)),
]