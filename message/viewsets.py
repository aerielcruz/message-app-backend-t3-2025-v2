from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from message.models import Chat_room, Message
from message.serializers import Chat_roomSerializer, MessageSerializer


class Chat_roomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Chat_room.objects.all()
    serializer_class = Chat_roomSerializer

    def get_queryset(self):
        # my_send_message = Message.objects.filter(sender=self.request.user)
        # my_receive_message = Message.objects.filter(receiver=self.request.user)
        # chatrooms = Chat_room.objects.filter(messages__in=my_send_message | my_receive_message)
        chatrooms = Chat_room.objects.filter(self.request.user)
        return chatrooms

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer