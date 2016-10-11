from rest_framework import serializers
from todo.models import TodoItem


class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
    """
    serializers class
    """
    url = serializers.ReadOnlyField()

    class Meta:
        """
        the meta class
        """
        model = TodoItem
        fields = ('url', 'title', 'completed', 'order')
