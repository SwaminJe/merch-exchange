from django.contrib import admin

from listings.models import Band, Article

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'sold', 'band')

admin.site.register(Band, BandAdmin)
admin.site.register(Article, ArticleAdmin)
