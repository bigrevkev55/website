from django.contrib import admin
from .models import Style, Boxer, Fight 

class StyleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class BoxerAdmin(admin.ModelAdmin):
    list_display = ('id','style', 'first_name', 'last_name', 'nick_name')

class FightAdmin(admin.ModelAdmin):
    list_display = ('id', 'red_corner_id', 'blue_corner_id', 'title_fight', 'scheduled_rounds', 'decision_round', 'decision_type', 'winner_id')

# Register your models here.
admin.site.register(Style, StyleAdmin)
admin.site.register(Boxer, BoxerAdmin)
admin.site.register(Fight, FightAdmin)