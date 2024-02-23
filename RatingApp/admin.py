from django.contrib import admin
from .models import RatingTable
from import_export.admin import ImportExportModelAdmin

# class RatingTableAdmin(admin.ModelAdmin):
#     list=['Name','p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15','p16','p17','p18','p19','p20','p21','p22','p23','p24','p25','p26','p27','p28','p29','p30',]
# admin.site.register(RatingTable,RatingTableAdmin)

@admin.register(RatingTable)

class IEAdmin(ImportExportModelAdmin):
    pass