from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from .models import User
from rest_framework.exceptions import APIException


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone', 'password')
        extra_kwargs = {
            'pasword': {'write_only': True},
        }
    #
    # def validate(self, attrs):
    #     phone = attrs['phone']
    #
    #     if User.objects.filter(phone=phone).exists():
    #         raise APIException("Bunaqa Foydalanuvchi mavjud")
    #     return attrs

    def create(self, validated_data):
        return User.objects.create_user(phone=validated_data['phone'], password=validated_data['password'])

