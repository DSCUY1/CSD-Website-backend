from rest_framework import serializers 
from .models import Event, Article, Information, Message
from users.models import User
from users.serializers import UsersSerializer
from rest_framework.serializers import SerializerMethodField
import datetime


class UserRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return UsersSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)

    
class EventSerializer(serializers.ModelSerializer):
    user = UserRelatedField(queryset=User.objects.all(), many=False)

    class Meta:
        model = Event
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    user = UserRelatedField(queryset=User.objects.all(), many=False)

    class Meta:
        model = Article
        fields = "__all__"


    
class InformationSerializer(serializers.ModelSerializer):
    user = UserRelatedField(queryset=User.objects.all(), many=False)

    class Meta:
        model = Information
        fields = "__all__"



class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
