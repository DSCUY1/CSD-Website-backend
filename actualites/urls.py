from django.urls import path
from .views import EventViewSet, ArticleViewSet, InformationViewSet, MessageViewSet


urlpatterns = [
    path("evenement" , EventViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('evenement/<str:pk>', EventViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("article" , ArticleViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('article/<str:pk>', ArticleViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("information" , InformationViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('information/<str:pk>', InformationViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("message" , MessageViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('message/<str:pk>', MessageViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
]