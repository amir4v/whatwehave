from django.contrib import admin
from .models import Year, Month, Day, Note


admin.site.register(Year)
admin.site.register(Month)
admin.site.register(Day)
admin.site.register(Note)