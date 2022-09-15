from rest_framework.serializers import ModelSerializer
from .models import Account, Character, Characteritem, Charactermakinglog, Friend, Login


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class CharacterSerializer(ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"


class CharacterItemSerializer(ModelSerializer):
    class Meta:
        model = Characteritem
        fields = "__all__"


class CharacterMakingSerializer(ModelSerializer):
    class Meta:
        model = Charactermakinglog
        fields = "__all__"


class FriendSerializer(ModelSerializer):
    class Meta:
        model = Friend
        fields = "__all__"


class LoginSerializer(ModelSerializer):
    class Meta:
        model = Login
        fields = "__all__"


