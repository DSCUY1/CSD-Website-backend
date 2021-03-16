from rest_framework import permissions
from .serializers import UsersSerializer


class ViewPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        data = UsersSerializer(request.data).data

        # donner le droit de voir
        view_acces = any(
            p['name'] == 'view_'+view.permission_object for p in data['role']['permissions'])
        # donner le droit d' editer
        edit_acces = any(
            p['name'] == 'edit_'+view.permission_object for p in data['role']['permissions'])

        if request.method == "GET":
            return view_acces or edit_acces
        return edit_acces
