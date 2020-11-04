from rest_framework import serializers
from .models import Todo


class TodoSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        #fileds = ('id','title','description','completed')