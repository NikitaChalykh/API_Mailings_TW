from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from mailings.models import Contact, Mailing, Message

from .serializers import (ContactSerializer, MailinglistSerializer,
                          MailingSerializer, MessageSerializer)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('tag', 'code')


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return MailinglistSerializer
        return MailingSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
