from django.contrib import admin
from .models import Dojo
from .models import Rank
from .models import CustomUser
from .models import Event
from .models import EventJoin
from .models import Favorite
from .models import PracticeRecord
from .models import ExaminationResult

# Register your models here.
admin.site.register(Dojo)
admin.site.register(Rank)
admin.site.register(CustomUser)
admin.site.register(Event)
admin.site.register(EventJoin)
admin.site.register(Favorite)
admin.site.register(PracticeRecord)
admin.site.register(ExaminationResult)
