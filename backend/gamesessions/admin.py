from django.contrib import admin
from .models import Game, SessionType, GameMod, GameNation, Session, SessionMod, SessionHost, SessionPlayer, PlayedNation

############################################################################################################################
######################################################### INLINES ##########################################################
############################################################################################################################

class GameNationInline(admin.TabularInline):
    model = GameNation
    extra = 0
class GameModInline(admin.TabularInline):
    model = GameMod
    extra = 0
class SessionModInline(admin.TabularInline):
    model = SessionMod
    extra = 0
class SessionHostInline(admin.TabularInline):
    model = SessionHost
    extra = 0
class SessionPlayerInline(admin.TabularInline):
    model = SessionPlayer
    extra = 0

############################################################################################################################
######################################################### PANELS ###########################################################
############################################################################################################################

class GameAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [GameNationInline, GameModInline]
class SessionTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
class SessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'game', 'sessiontype', 'date', 'hasBegun', 'is_recent']
    inlines = [SessionModInline, SessionHostInline, SessionPlayerInline]
class PlayedNationAdmin(admin.ModelAdmin):
    list_display = ['sessionplayer', 'gamenation']


admin.site.register(Game, GameAdmin)
admin.site.register(SessionType, SessionTypeAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(PlayedNation, PlayedNationAdmin)