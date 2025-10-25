from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user( # type: ignore
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data[' password']
        )

        user.is_active = False
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError('Username yoki password xato')
        if not user.is_active:
            raise serializers.ValidationError('Account aktiv emas. Iltimos emailni tasdiqlang.')
        attrs['user'] = user
        return attrs