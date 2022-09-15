from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import AccountSerializer, CharacterSerializer
from .models import Account, Character

from members.logic.service import max_out_account
from members.logic.selectors import list_accounts, list_characters



class AccountList(APIView):
    def get(self, request):
        ret = AccountSerializer(instance=list_accounts(), many=True)
        return Response(ret.data)

class CharacterList(APIView):
    def get(self, request):
        ret = CharacterSerializer(instance=list_characters(), many=True)
        return Response(ret.data)


class CharacterViewSet(ModelViewSet):
    queryset         = Character.objects.all()
    serializer_class = CharacterSerializer


class MaxOutAccount(APIView):
    class InputSerializer(serializers.Serializer):
        account_id = serializers.IntegerField()
        target_level = serializers.IntegerField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        max_out_account(**serializer.validated_data)
        return Response({"suc": "noice"})
