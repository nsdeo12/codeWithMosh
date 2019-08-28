from django.contrib import admin
from .models import Genre,Movie

class GenreAdmin(admin.ModelAdmin):
    list_display=('id','name')

class MovieAdmin(admin.ModelAdmin):
    exclude=('date_created',)
    
    list_display=('id','title','release_year','number_in_stock','genre','daily_rate')

# Register your models here.
admin.site.register(Genre,GenreAdmin)
admin.site.register(Movie,MovieAdmin)
