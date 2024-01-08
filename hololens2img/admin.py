from django.contrib import admin
from hololens2img.models import MS1, MS2, MS3, MS4, MS5, MS6, WH


class AbstractImageModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'label', 'order', 'image')
    ordering = ('order',)


admin.site.register(MS1, AbstractImageModelAdmin)
admin.site.register(MS2, AbstractImageModelAdmin)
admin.site.register(MS3, AbstractImageModelAdmin)
admin.site.register(MS4, AbstractImageModelAdmin)
admin.site.register(MS5, AbstractImageModelAdmin)
admin.site.register(MS6, AbstractImageModelAdmin)
admin.site.register(WH, AbstractImageModelAdmin)
