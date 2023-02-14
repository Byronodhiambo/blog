from django.urls import path
from .views import ThreadList, ThreadDetail, PostList, PostDetail, MessageList, MessageDetail, RelationshipList, RelationshipDetail, EventDetail, EventList


urlpatterns = [
    path('threads/', ThreadList.as_view(), name='thread-list'),
    path('threads/<int:pk>/', ThreadDetail.as_view(), name='thread-detail'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('messages/', MessageList.as_view(), name='message-list'),
    path('messages/<int:pk>/', MessageDetail.as_view(), name='message-detail'),
    path('relationships/', RelationshipList.as_view(), name='relationship-list'),
    path('relationships/<int:pk>/', RelationshipDetail.as_view(), name='relationship-detail'),
    path('events/', EventList.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
    
]
