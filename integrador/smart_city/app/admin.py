from django.contrib import admin
from .models import Ambientes, Historico, Sensores


admin.site.register(Ambientes)
admin.site.register(Historico)
admin.site.register(Sensores)