from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from quickstart.serializers import GroupSerializer, UserSerializer

from django.http import HttpResponse


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def index_view(request):
    return HttpResponse("Hello, Django.")


def test_index_view(rf):
    request = rf.get("/")
    response = index_view(request)
    assert response.content == b"Hello, Django."
