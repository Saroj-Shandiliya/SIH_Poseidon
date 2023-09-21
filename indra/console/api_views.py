# console/api_views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ClassifiedWaterFlowData
from .serializers import ClassifiedWaterFlowDataSerializer

@api_view(['GET'])
def get_classified_data(request):
    classified_data = ClassifiedWaterFlowData.objects.all()
    serializer = ClassifiedWaterFlowDataSerializer(classified_data, many=True)
    return Response(serializer.data)

from django.http import JsonResponse

def check_authentication(request):
    is_authenticated = request.user.is_authenticated
    return JsonResponse({'isAuthenticated': is_authenticated})
