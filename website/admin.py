from django.contrib import admin
from .models import Record,gestionTickets,responsablesAtencion,contactoTipo

admin.site.register(Record)
admin.site.register(gestionTickets)
admin.site.register(responsablesAtencion)
admin.site.register(contactoTipo)


