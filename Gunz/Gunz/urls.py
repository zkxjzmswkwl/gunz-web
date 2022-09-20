from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from members.views import MaxOutAccount, AccountList, CharacterList, GameRoomList
from clans.views import ClanList, ClanListByPoints, ClanListByTotalPoints, ClanMemberList, AdminAbuse, ClanReset

# r = routers.DefaultRouter()
# r.register(r'characters', CharacterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # List
    path("gunz/accounts/list/",               AccountList.as_view(),           name="list"),
    path("gunz/characters/list/",             CharacterList.as_view(),         name="list"),
    path("gunz/clans/list/",                  ClanList.as_view(),              name="list"),
    path("gunz/clans/list/totalpoints/",      ClanListByTotalPoints.as_view(), name="list"),
    path("gunz/clans/list/points/",           ClanListByPoints.as_view(),      name="list"),
    path("gunz/clans/<int:clan_id>/members/", ClanMemberList.as_view(),        name="list"),
    path("gunz/stages/list",                  GameRoomList.as_view(),          name="list"),


    # Create
    path("gunz/maxoutaccount/",     MaxOutAccount.as_view(), name='create'),
    path("gunz/clans/adminaboose/", AdminAbuse.as_view(),    name='create'),
    path("gunz/clans/reset/",       ClanReset.as_view(),     name='create'),

    # Update

    # Detail
]
