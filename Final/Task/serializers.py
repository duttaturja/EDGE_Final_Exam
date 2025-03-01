# from rest
from rest_framework import serializers

# from models
from Task.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'