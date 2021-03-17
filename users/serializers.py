from django.db.models.fields import DateTimeCheckMixin
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import User, Role, Permission
import datetime


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class PermissionRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return PermissionSerializer(value).data

    def to_internal_value(self, data):
        return data


class RoleRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return RoleSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionRelatedField(many=True)

    class Meta:
        model = Role
        fields = "__all__"

    def create(self, validated_data):
        permissions = validated_data.pop('permissions', None)
        # return a dictionnary
        instance = self.Meta.model(**validated_data)
        instance.save()
        # normal array
        instance.permissions.add(*permissions)
        instance.save()
        return instance


class UsersSerializer(serializers.ModelSerializer):
    role = RoleRelatedField(queryset=Role.objects.all(), many=False)
    surv = SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'password',
            "matricule",
            'role',
            "surv",
            'types',
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }
    # Methode pour
    def get_surv(self, obj):
        presents = obj.user_control.all()
        current_date = datetime.datetime.now().date()
        
        result = {
                    "present":[],
                    "absent":[]
                }

        for present in presents :
        
            item = {
                'surv': {
                    "id" : present.surveillant.id,
                    "matricule" : present.surveillant.matricule,
                    "nom" : present.surveillant.first_name +" "+  present.surveillant.last_name
                },
                
                'niveau' : {
                            'id' : present.examen.ue.level.id,
                            'niveau' : present.examen.ue.level.level,
                            'filiere': present.examen.ue.level.filiere.name,
                        },
                
                'salle' : {
                            'id' : present.salle.id,
                            'code': present.salle.code,
                            'localisation': present.salle.localisation
                        },
                
                'Ue' : {
                        "id": present.examen.id,
                        "code": present.examen.ue.code,
                        "intitule": present.examen.ue.intitule,
                    },
                
                'Horaire' : {
                    'id' : present.examen.plage.id,
                    "date": present.examen.day,
                    'begin' : present.examen.plage.begin,
                    'end' : present.examen.plage.end
                }
            }

            if current_date <= present.examen.day :
                if present.is_present:
                    result["present"].append(item)
                else:
                    result["absent"].append(item)
        return result

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # retourner un dictionnaire
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        # retourner un dictionnaire
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
