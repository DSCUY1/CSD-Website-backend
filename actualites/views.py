from django.db.models import Q
import datetime
from django.shortcuts import render
from .models import Event, Article, Information, Message
from rest_framework.response import Response
from .serializers import EventSerializer, ArticleSerializer, InformationSerializer, MessageSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import exceptions, status, generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from users.authentication import JwtAuthenticatedUser
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from django.http import HttpResponse



class EventViewSet(viewsets.ViewSet):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = EventSerializer(Event.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        event= Event.objects.get(id=pk)
        serializer = EventSerializer(event)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        event = Event.objects.get(id=pk)
        serializer = EventSerializer(instance=event, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        event = Event.objects.get(id=pk)
        event.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)




class ArticleViewSet(viewsets.ViewSet):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = ArticleSerializer(Article.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        article= Article.objects.get(id=pk)
        serializer = ArticleSerializer(article)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        article = Article.objects.get(id=pk)
        serializer = ArticleSerializer(instance=article, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        article = Article.objects.get(id=pk)
        article.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)




class InformationViewSet(viewsets.ViewSet):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = InformationSerializer(Information.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        information= Information.objects.get(id=pk)
        serializer = InformationSerializer(information)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = InformationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        information = Information.objects.get(id=pk)
        serializer = InformationSerializer(instance=information, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        information = Information.objects.get(id=pk)
        information.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)




class MessageViewSet(viewsets.ViewSet):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = MessageSerializer(Message.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        message= Message.objects.get(id=pk)
        serializer = MessageSerializer(message)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        message = Message.objects.get(id=pk)
        serializer = MessageSerializer(instance=message, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        message = Message.objects.get(id=pk)
        Message.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)