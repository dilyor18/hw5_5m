from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer
from .permissions import IsOwnerOrReadOnly



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        order = self.get_object()

        if order.status != 'created':
            return Response({'error': 'Нельзя принять'}, status=400)

        order.status = 'accepted'
        order.save()
        return Response({'status': 'accepted'})

    @action(detail=True, methods=['post'])
    def close(self, request, pk=None):
        order = self.get_object()

        if order.status != 'accepted':
            return Response({'error': 'Нельзя закрыть'}, status=400)

        order.status = 'closed'
        order.save()
        return Response({'status': 'closed'})


