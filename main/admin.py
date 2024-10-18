from django.contrib import admin
from .models import Dojo
from .models import Rank
from .models import CustomUser
from .models import Event
from .models import EventJoin
from .models import Favorite
from .models import PracticeRecord
from .models import ExaminationResult

class DojoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)

class RankAdmin(admin.ModelAdmin):
    list_display = ('id', 'rank',)
    search_fields = ('rank',)
    
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname',)
    search_fields = ('nickname',)
    
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    
class EventJoinAdmin(admin.ModelAdmin):
    list_display = ('id', 'status',)
    search_fields = ('status',)
    
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
    search_fields = ('user',)
    
class PracticeRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
    search_fields = ('user',)
    
class ExaminationResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
    search_fields = ('user',)

# Register your models here.
admin.site.register(Dojo,DojoAdmin)
admin.site.register(Rank,RankAdmin)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(EventJoin,EventJoinAdmin)
admin.site.register(Favorite,FavoriteAdmin)
admin.site.register(PracticeRecord,PracticeRecordAdmin)
admin.site.register(ExaminationResult,ExaminationResultAdmin)
