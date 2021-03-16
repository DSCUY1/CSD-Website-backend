from django.shortcuts import render
from rest_framework import exceptions, viewsets, status,generics, mixins
from .models import User, Permission, Role
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import UsersSerializer, PermissionSerializer, RoleSerializer
from .models import User, Permission, Role
from .authentication import access_tokens, JwtAuthenticatedUser
from .permissions import ViewPermission


@api_view(['post'])
def signup(request):
    data = request.data
    if data['password'] != data["password_confirm"]:
        raise exceptions.APIException("le mot de passe ne convient pas")
    serializer = UsersSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


# Methode signin
@api_view(['post'])
def signin(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed("user is not found ")
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed("incorret password")

    response = Response()
    # je genere le json web tken
    token = access_tokens(user)
    #  je set le cookie
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response

# j ' obtiens l 'authenticated user


class AuthenticateUSer(APIView):
    authentication_classes = [JwtAuthenticatedUser]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = UsersSerializer(request.user).data
        data['permissions'] = [p['name'] for p in data['role']['permissions']]
        return Response({
            'data': data
        })


@api_view(['post'])
def signout(reques):
    response = Response()
    response.delete_cookie(key='jwt')
    response.data = {
        "detail": "success"
    }
    return response


@api_view(['GET'])
def users(reques):
    serializer = UsersSerializer(User.objects.all(), many=True)
    return Response(serializer.data)

# Obtenir les permissions


class PermissionViewSet(viewsets.ViewSet):
    authentication_classes = [JwtAuthenticatedUser]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)
        return Response({
            "data": serializer.data
        })

    def create(self, request):
        serializer = PermissionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "data": serializer.data
        })

# Definir un viewSet Pour gerer les Roles


class RoleViewSet(viewsets.ViewSet):
    authentication_classes = [JwtAuthenticatedUser]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = RoleSerializer(Role.objects.all(), many=True)
        return Response({
            "data": serializer.data
        })

    def retrieve(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(role)
        return Response({
            "data": serializer.data
        })

    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "data": serializer.data
        })

    def update(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(instance=role, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "deta": serializer.data
        }, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk=None):
        role = Role.objects.get(id=pk)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class UserGenericAPIVIEW(generics.GenericAPIView,
#                          mixins.ListModelMixin, mixins.RetrieveModelMixin,
#                          mixins.CreateModelMixin, mixins.UpdateModelMixin,
#                          mixins.DestroyModelMixin):
#     # authentication_classes = [JwtAuthenticatedUser]
#     # permission_classes = [IsAuthenticated]  
#     queryset = User.objects.all()
#     serializer_class = UsersSerializer

#     def get(self, request, pk=None):
#         if pk:
#             return Response({'data': self.retrieve(request, pk).data})
#         return Response({
#             'data': self.list(request).data
#         })

#     def post(self, request):
#         return Response({
#             "data": self.create(request).data
#         })

#     def put(self, request, pk=None):
#         return Response({
#             "data": self.partial_update(request, pk).data
#         })

#     def delete(self, request, pk=None):
#         return self.destroy(request, pk)


#     def update(self, request, pk=None):
#         user = Users.objects.get(id=pk)
#         serializer = UsersSerializer(instance=user, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             "data": serializer.data
#         }, status=status.HTTP_202_ACCEPTED)

#     def delete(self, request, pk=None):
#         user = Users.objects.get(id=pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)






class UserViewSet(viewsets.ViewSet):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = UsersSerializer(User.objects.all(), many=True)
        return Response({
            "data": serializer.data
        })

    def retrieve(self, request, pk=None):
        user = User.objects.get(id=pk)
        serializer = UsersSerializer(user)
        return Response({
            "data": serializer.data
        })

    def create(self, request):
        serializer = UsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "data": serializer.data
        })

    def update(self, request, pk=None):
        user = User.objects.get(id=pk)
        serializer = UsersSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "deta": serializer.data
        }, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk=None):
        user = User.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
