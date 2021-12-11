from rest_framework import serializers

from chats.models import Chat, Message


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class ChatMessagesSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(read_only=True, source='message_set', many=True)

    class Meta:
        model = Chat
        fields = '__all__'
