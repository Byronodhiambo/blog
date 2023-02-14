from rest_framework import generics
from .models import Thread, Post, Message, Relationship, Event
from .serializers import ThreadSerializer, PostSerializer, MessageSerializer, RelationshipSerializer, EventSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ThreadList(generics.ListCreateAPIView):     
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

class ThreadDetail(generics.RetrieveUpdateDestroyAPIView):     
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

class PostList(generics.ListCreateAPIView):     
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):     
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class MessageList(generics.ListCreateAPIView):     
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):     
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class RelationshipList(generics.ListCreateAPIView):     
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer

class RelationshipDetail(generics.RetrieveUpdateDestroyAPIView):     
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer


class EventList(generics.ListCreateAPIView):     
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):     
    queryset = Event.objects.all()
    serializer_class = EventSerializer
