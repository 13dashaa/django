from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from users.models import Subscription

User = get_user_model()


class CustomUserSerializer(UserSerializer):
    """Сериализатор пользователей."""

    class Meta:
        model = User
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор подписки."""

    # TODO
    lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = ('title', 'author', 'price'
            # TODO
        )


    def count_lessons(self, obj):
        return obj.lesson_set.count()
