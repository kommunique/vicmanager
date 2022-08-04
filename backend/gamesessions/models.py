from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone
from django.utils.timezone import now

import datetime


class Game(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

class SessionType(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

class GameMod(models.Model):
    name = models.CharField(max_length=100)
    nameshort = models.CharField(max_length=30)
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    class Meta:
        ordering = ['game', 'name']
    def __str__(self):
        return self.name

class GameNation(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=30)
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

class Session(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField('date announced', default=now)
    hasBegun = models.BooleanField(default=False)
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    sessiontype = models.ForeignKey(SessionType, on_delete=models.PROTECT)

    class Meta:
        ordering = ['date', 'game', 'sessiontype', 'name']
    def __str__(self):
        return self.name
    """
    @admin.display(
        boolean=True,
        ordering='date',
        description='recent?',
    )
    """
    def is_recent(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.date <= now


class SessionMod(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    mod = models.ForeignKey(GameMod, on_delete=models.SET_NULL, null=True)
    class Meta:
        ordering = ['session']
    def __str__(self):
        return (self.session.name + ":" + self.mod.name)

class SessionHost(models.Model):
    isMainHost = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    class Meta:
        ordering = ['session', 'isMainHost', 'user']
    def __str__(self):
        return self.user.username

class SessionPlayer(models.Model):
    isDone = models.BooleanField(default=False)
    order = models.CharField(max_length=100, default=0)
    savefile=models.FileField(default=None, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)


    class Meta:
        ordering = ['session', 'order', 'user']
    def __str__(self):
        return self.user.username

class PlayedNation(models.Model):
    sessionplayer = models.ForeignKey(SessionPlayer, on_delete=models.PROTECT)
    gamenation = models.ForeignKey(GameNation, on_delete=models.PROTECT)

    class Meta:
        ordering = ['sessionplayer', 'gamenation']
    def __str__(self):
        return (self.sessionplayer.user.username + ":" + self.gamenation.name)