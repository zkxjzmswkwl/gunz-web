from django.db import models


class Clan(models.Model):
    clid             = models.AutoField(db_column='CLID', primary_key=True)  # Field name made lowercase.
    name             = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    exp              = models.IntegerField(db_column='Exp')  # Field name made lowercase.
    level            = models.IntegerField(db_column='Level')  # Field name made lowercase.
    point            = models.IntegerField(db_column='Point')  # Field name made lowercase.
    mastercid        = models.IntegerField(db_column='MasterCID', blank=True, null=True)  # Field name made lowercase.
    wins             = models.IntegerField(db_column='Wins')  # Field name made lowercase.
    markwebimg       = models.TextField(db_column='MarkWebImg', blank=True, null=True)  # Field name made lowercase.
    introduction     = models.TextField(db_column='Introduction', blank=True, null=True)  # Field name made lowercase.
    regdate          = models.TextField(db_column='RegDate')  # Field name made lowercase.
    deleteflag       = models.TextField(db_column='DeleteFlag', blank=True, null=True)  # Field name made lowercase.
    deletename       = models.TextField(db_column='DeleteName', blank=True, null=True)  # Field name made lowercase.
    homepage         = models.TextField(db_column='Homepage', blank=True, null=True)  # Field name made lowercase.
    losses           = models.IntegerField(db_column='Losses')  # Field name made lowercase.
    draws            = models.IntegerField(db_column='Draws')  # Field name made lowercase.
    ranking          = models.IntegerField(db_column='Ranking')  # Field name made lowercase.
    totalpoint       = models.IntegerField(db_column='TotalPoint')  # Field name made lowercase.
    cafe_url         = models.TextField(db_column='Cafe_Url', blank=True, null=True)  # Field name made lowercase.
    email            = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    emblemurl        = models.TextField(db_column='EmblemUrl', blank=True, null=True)  # Field name made lowercase.
    rankincrease     = models.IntegerField(db_column='RankIncrease')  # Field name made lowercase.
    emblemchecksum   = models.IntegerField(db_column='EmblemChecksum')  # Field name made lowercase.
    lastdayranking   = models.IntegerField(db_column='LastDayRanking')  # Field name made lowercase.
    lastmonthranking = models.IntegerField(db_column='LastMonthRanking')  # Field name made lowercase.

    def __str__(self):
        return f"{self.clid}:{self.name}"

    class Meta:
        managed  = False
        db_table = 'Clan'


class Clanmember(models.Model):
    cmid      = models.AutoField(db_column='CMID', primary_key=True)  # Field name made lowercase.
    clid      = models.IntegerField(db_column='CLID', blank=True, null=True)  # Field name made lowercase.
    cid       = models.IntegerField(db_column='CID', blank=True, null=True)  # Field name made lowercase.
    grade     = models.IntegerField(db_column='Grade')  # Field name made lowercase.
    regdate   = models.TextField(db_column='RegDate')  # Field name made lowercase.
    contpoint = models.IntegerField(db_column='ContPoint')  # Field name made lowercase.

    class Meta:
        managed  = False
        db_table = 'ClanMember'


