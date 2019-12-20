from django.contrib import admin
from .models import movies_detail
from .models import event_detail


# Register your models here.
admin.site.register(movies_detail)
admin.site.register(event_detail)
