from django.contrib import admin

# Register your models here.

from .models import Tutor, Specialty

class TutorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tutor Name Selection',               {'fields': ['screen_name']}),
        ('Initial Teaching Date',              {'fields': ['teaching_start_date']}),
        ('Tutor Email',                        {'fields': ['teacher_email']}),
        ('Tutor Address',                      {'fields': ['teacher_address']}),
        ('Tutor Photo',                        {'fields': ['tutor_photo']}),

    ]

admin.site.register(Tutor, TutorAdmin)
admin.site.register(Specialty)