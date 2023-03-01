from rest_framework.viewsets import ModelViewSet
from . import models, serializers


class StudentView(ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
