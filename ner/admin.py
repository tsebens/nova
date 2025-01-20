from django.contrib import admin

from ner.models import Text, Mention, Entity

# Register your models here.
admin.site.register(Text)
admin.site.register(Mention)
admin.site.register(Entity)
