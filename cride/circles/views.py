"""Circles views."""

# Django REST
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Models
from cride.circles.models import Circle
# Sercializer
from cride.circles.serializers import (
    CircleSerializer,
    CreateCircleSerializer
    )

@api_view(['GET'])
def list_circles(request):
    """List circles."""
    # import ipdb; ipdb.set_trace()
    
    circles = Circle.objects.filter(is_public=True)
    serializer = CircleSerializer(circles, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_circle(request):
    """Create circle."""
    serializer = CreateCircleSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    circle = serializer.save()
    return Response(CircleSerializer(circle).data)
