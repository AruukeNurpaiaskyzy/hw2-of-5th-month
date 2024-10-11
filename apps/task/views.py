from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


from .models import Task
from .serializers  import TaskSerializers
# Create your views here.
class TaskAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
