from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'auction', 'image', 'updated_date']
=======
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'auction', 'updated_date']
>>>>>>> aff0d0f9e223afdb28d9be9e84e4540b2ddc44f9
    list_filter = ['created_at', 'price']
    actions = ['make_auction_false', 'make_auction_true']
    fieldsets = (
        ('Общее', {
            'fields' : ('title', 'description', 'image'), 
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
