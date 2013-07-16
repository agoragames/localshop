from rest_framework import viewsets, serializers, filters
from localshop.apps.packages.models import Package, Release, ReleaseFile
from django.utils.decorators import method_decorator
from localshop.apps.permissions.utils import credentials_required

class CredentialRequiredMixin(object):

    @method_decorator(credentials_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CredentialRequiredMixin, self).dispatch(request, *args, **kwargs)

class PackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Package
        fields = (
            'created',
            'name',
            'is_local'
        )

class ReleaseFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReleaseFile
        fields = (
            'filetype',
            'filename',
            'md5_digest',
            'python_version'
        )

class ReleaseSerializer(serializers.ModelSerializer):

    package = PackageSerializer()
    files = ReleaseFileSerializer()

    class Meta:
        model = Release
        fields = (
            'id',
            'created',
            'version',
            'package',
            'files'
        )


class LocalReleasesViewset(CredentialRequiredMixin, viewsets.ReadOnlyModelViewSet):
    model = Release
    serializer_class = ReleaseSerializer
    lookup_field = 'package__name'

    def get_queryset(self):
        return Release.objects.filter(package__is_local=True)

