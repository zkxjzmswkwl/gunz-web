from django.db import models


class Account(models.Model):
    aid      = models.AutoField(db_column='AID', primary_key=True)  # Field name made lowercase.
    userid   = models.TextField(db_column='UserID', unique=True, blank=True, null=True)  # Field name made lowercase.
    ugradeid = models.IntegerField(db_column='UGradeID', blank=True, null=True)  # Field name made lowercase.
    pgradeid = models.IntegerField(db_column='PGradeID', blank=True, null=True)  # Field name made lowercase.
    email    = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    regdate  = models.DateTimeField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"{self.userid} - {self.email} - {self.regdate}"

    class Meta:
        managed  = False
        db_table = 'Account'


class Character(models.Model):
    cid           = models.AutoField(db_column='CID', primary_key=True)  # Field name made lowercase.
    aid           = models.IntegerField(db_column='AID')  # Field name made lowercase.
    name          = models.TextField(db_column='Name')  # Field name made lowercase.
    level         = models.IntegerField(db_column='Level')  # Field name made lowercase.
    sex           = models.IntegerField(db_column='Sex')  # Field name made lowercase.
    charnum       = models.IntegerField(db_column='CharNum')  # Field name made lowercase.
    hair          = models.IntegerField(db_column='Hair', blank=True, null=True)  # Field name made lowercase.
    face          = models.IntegerField(db_column='Face', blank=True, null=True)  # Field name made lowercase.
    xp            = models.IntegerField(db_column='XP')  # Field name made lowercase.
    bp            = models.IntegerField(db_column='BP')  # Field name made lowercase.
    items         = models.BinaryField(db_column='Items', blank=True, null=True)  # Field name made lowercase.
    regdate       = models.TextField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    lasttime      = models.TextField(db_column='LastTime', blank=True, null=True)  # Field name made lowercase.
    playtime      = models.IntegerField(db_column='PlayTime', blank=True, null=True)  # Field name made lowercase.
    gamecount     = models.IntegerField(db_column='GameCount', blank=True, null=True)  # Field name made lowercase.
    killcount     = models.IntegerField(db_column='KillCount', blank=True, null=True)  # Field name made lowercase.
    deathcount    = models.IntegerField(db_column='DeathCount', blank=True, null=True)  # Field name made lowercase.
    deleteflag    = models.IntegerField(db_column='DeleteFlag', blank=True, null=True)  # Field name made lowercase.
    deletename    = models.TextField(db_column='DeleteName', blank=True, null=True)  # Field name made lowercase.
    questiteminfo = models.BinaryField(db_column='QuestItemInfo', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"{self.name} ({self.level}) - {self.lasttime} ({self.playtime})"

    class Meta:
        managed  = False
        db_table = 'Character'


class Characteritem(models.Model):
    ciid           = models.AutoField(db_column='CIID', primary_key=True)  # Field name made lowercase.
    cid            = models.IntegerField(db_column='CID', blank=True, null=True)  # Field name made lowercase.
    itemid         = models.IntegerField(db_column='ItemID')  # Field name made lowercase.
    regdate        = models.IntegerField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    rentdate       = models.IntegerField(db_column='RentDate', blank=True, null=True)  # Field name made lowercase.
    renthourperiod = models.IntegerField(db_column='RentHourPeriod', blank=True, null=True)  # Field name made lowercase.
    cnt            = models.IntegerField(db_column='Cnt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed  = False
        db_table = 'CharacterItem'


class Charactermakinglog(models.Model):
    aid      = models.IntegerField(db_column='AID', blank=True, null=True)  # Field name made lowercase.
    charname = models.TextField(db_column='CharName', blank=True, null=True)  # Field name made lowercase.
    type     = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    date     = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed  = False
        db_table = 'CharacterMakingLog'


class Friend(models.Model):
    cid        = models.IntegerField(db_column='CID')  # Field name made lowercase.
    friendcid  = models.IntegerField(db_column='FriendCID')  # Field name made lowercase.
    type       = models.IntegerField(db_column='Type')  # Field name made lowercase.
    favorite   = models.IntegerField(db_column='Favorite', blank=True, null=True)  # Field name made lowercase.
    deleteflag = models.IntegerField(db_column='DeleteFlag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed  = False
        db_table = 'Friend'


class Login(models.Model):
    aid          = models.IntegerField(db_column='AID')  # Field name made lowercase.
    userid       = models.TextField(db_column='UserID', unique=True, blank=True, null=True)  # Field name made lowercase.
    passworddata = models.TextField(db_column='PasswordData', blank=True, null=True)  # Field name made lowercase.
    lastconndate = models.TextField(db_column='LastConnDate', blank=True, null=True)  # Field name made lowercase.
    lastip       = models.TextField(db_column='LastIP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed  = False
        db_table = 'Login'


class Gamerooms(models.Model):
    id          = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    title       = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    creator     = models.TextField(db_column='Creator', blank=False, null=False)  # Field name made lowercase.
    map         = models.TextField(db_column='Map')  # Field name made lowercase.
    mode        = models.TextField(db_column='Mode')  # Field name made lowercase.
    playercount = models.IntegerField(db_column='PlayerCount')  # Field name made lowercase.
    
    def __str__(self):
        return f"{self.creator} created stage \"{self.title}\" on map {self.map}"

    class Meta:
        managed  = False
        db_table = 'GameRooms'


