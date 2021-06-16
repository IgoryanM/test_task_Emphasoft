from django.contrib.auth.hashers import make_password
from rest_framework.serializers import HyperlinkedModelSerializer

from users.models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'password', 'first_name', 'last_name', 'email', 'age')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserModelSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserModelSerializer, self).update(instance, validated_data)
