from django.contrib import admin
from hotel.models import Hotel, Booking, ActivityLog, StaffOnDuty,Room, RoomType,HotelGallery, HotelFaqs, HotelFeatures



class HotelGalleryInline(admin.TabularInline):
    model=HotelGallery

class HotelAdmin(admin.ModelAdmin):
    inlines=[HotelGalleryInline]
    list_display=['thumbnail','name','user', 'status']
    prepopulated_fields={"slug":("name",)}

class BookingAdmin(admin.ModelAdmin):
    list_display=['full_name','check_in_date','check_out_date','user', 'payment_status', 'email',]

class ActivityLogAdmin(admin.ModelAdmin):
    list_display=['booking','guest_out','guest_in', 'description','date']

class StaffOnDutyAdmin(admin.ModelAdmin):
    list_display=['booking','staff_id','date']

class RoomAdmin(admin.ModelAdmin):
    list_display=['hotel','room_type','room_number', 'is_available','rid','date']

class RoomTypeAdmin(admin.ModelAdmin):
    list_display=['hotel','number_of_beds','room_capacity', 'date','type']


class HotelFaqsAdmin(admin.ModelAdmin):
    list_display=['hotel','question','answer', 'date']

class HotelFeaturesAdmin(admin.ModelAdmin):
    list_display=['hotel','icon_type','icon', 'name']



admin.site.register(Hotel, HotelAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(StaffOnDuty, StaffOnDutyAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(RoomType, RoomTypeAdmin)
# admin.site.register(HotelGallery, HotelGalleryInline)
admin.site.register(HotelFaqs, HotelFaqsAdmin)
admin.site.register(HotelFeatures, HotelFeaturesAdmin)

