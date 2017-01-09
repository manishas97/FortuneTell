from rest_framework import serializers

from polls import models

class MessageSerializer(serializers.ModelSerializer):
    """A serializer for our messages model."""

    class Meta:
        model = models.Message
        fields = ('messages')
