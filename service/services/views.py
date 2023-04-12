from rest_framework import viewsets

from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionView(viewsets.ReadOnlyModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
