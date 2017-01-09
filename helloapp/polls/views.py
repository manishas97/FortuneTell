from random import randint

from django.shortcuts import render
from django.db.models import Count

from rest_framework import views
from rest_framework.response import Response

from . import serializers, models

from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('index.html')

class MessageView(views.APIView):
    """View to managing messages through the API."""


    serializer_class = serializers.MessageSerializer

    def post(self, request, format=None):
        """Receive the post of the new messages and return a random one."""

        random_messages = self._get_random_messages()

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()


        random_messages.is_read = True
        random_messages.save()

        return Response(self.serializer_class(random_messages).data)

    def _get_random_messages(self):
        """Get a Random Message from the Database."""

        count = models.Message.objects.filter(
            is_read=False
        ).aggregate(
            count=Count('id')
        )['count']

        # Get a random number between the count.
        random_index = randint(0, count - 1)
        # Select the unread messages for the random number that was selected.
        random_messages = models.Message.objects.filter(
            is_read=False)[random_index]

        # Return the random_messages.
        return random_messages
