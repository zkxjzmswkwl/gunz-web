from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response

from .serializers import ClanSerializer, ClanMemberSerializer
from clans.logic.selectors import list_clans_by_wins, list_clans_by_points, list_clans_by_total_points, get_members_for
from clans.logic.service import admin_abuse


class ClanList(APIView):
    def get(self, request):
        ret = ClanSerializer(instance=list_clans_by_wins(), many=True)
        return Response(ret.data)


class ClanListByPoints(APIView):
    def get(self, request):
        ret = ClanSerializer(instance=list_clans_by_points(), many=True)
        return Response(ret.data)


class ClanListByTotalPoints(APIView):
    def get(self, request):
        ret = ClanSerializer(instance=list_clans_by_total_points(), many=True)
        return Response(ret.data)


class ClanMemberList(APIView):
    def get(self, request, clan_id):
        ret = ClanMemberSerializer(get_members_for(clan_id=clan_id), many=True)
        return Response(ret.data)
        

class AdminAbuse(APIView):
    class InputSerializer(serializers.Serializer):
        clan_id = serializers.IntegerField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        admin_abuse(**serializer.validated_data)
        return Response({"asjdflaskdfasdf": "8===D"})


