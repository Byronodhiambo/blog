from rest_framework import generics, permissions
from .models import Thread, Post, Message, Relationship, Event
from .serializers import ThreadSerializer, PostSerializer, MessageSerializer, RelationshipSerializer, EventSerializer, UserSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView



# Create your views here.

class ThreadList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)     
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

class ThreadDetail(generics.RetrieveUpdateDestroyAPIView): 
    permission_classes = (IsAuthenticated,)    
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

class PostList(generics.ListCreateAPIView): 
    permission_classes = (IsAuthenticated,)    
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView): 
    permission_classes = (IsAuthenticated,)    
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class MessageList(generics.ListCreateAPIView):     
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageDetail(generics.RetrieveUpdateDestroyAPIView): 
    permission_classes = (IsAuthenticated,)    
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class RelationshipList(generics.ListCreateAPIView):     
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer

class RelationshipDetail(generics.RetrieveUpdateDestroyAPIView): 
    permission_classes = (IsAuthenticated,)    
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer


class EventList(generics.ListCreateAPIView):     
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView): 
    permission_classes = (IsAuthenticated,)    
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)