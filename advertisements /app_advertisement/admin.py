from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'auction', 'updated_date']
    list_filter = ['created_at', 'price']
    actions = ['make_auction_false', 'make_auction_true']
    fieldsets = (
        ('Общее', {
            'fields' : ('title', 'description'), 
            'classes' : ['collapse']
        }), 

        ('Финансы', {
            'fields' : ('price', 'auction'), 
            'classes' : ['collapse']
        })
    )

    @admin.action(description='Убрать все торги')
    def make_auction_false(self, request, queryset):
        queryset.update(auction = False)

    @admin.action(description='Проставить возможность торгов')
    def make_auction_true(self, request, queryset):
        queryset.update(auction = True)



admin.site.register(Advertisement, AdvertisementAdmin)
# Register your models here.
