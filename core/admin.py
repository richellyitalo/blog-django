from django.contrib import admin

from .models import Post, Page, Banner

# Register your models here.


class BannerAdmin(admin.ModelAdmin):
    exclude = ('sort_order', )


admin.site.register(Post)
admin.site.register(Page)
admin.site.register(Banner, BannerAdmin)
