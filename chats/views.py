from rest_framework import viewsets
from rest_framework.response import Response

from chats import serializers
from chats.models import Chat, Message
from chats.serializers import ChatMessagesSerializer


class ChatView(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = serializers.ChatSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ChatMessagesSerializer(instance)
        return Response(serializer.data)


class MessageView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer
