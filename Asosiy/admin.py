from django.contrib import admin

from .models import *


class TalabaAdmin(admin.ModelAdmin):
    list_display = ["id","ism","kurs","kitob_soni"]
    list_display_links = ["id","ism"]
    list_editable = ["kurs" , "kitob_soni"]
    list_filter = ["kurs"]
    search_fields = ["ism", "id"]
    search_help_text = "ID va ism boyicha qidiring."
    list_per_page = 4



# class MuallifAdmin(admin.ModelAdmin):
#     list_display = ["id","ism", "jins", "tugilgan_sana","kitoblar_soni","tirik"]
#     list_display_links = ["id"]
#     list_editable = ["kitoblar_soni"]
#     search_fields = ["ism","id"]
#     list_filter = ["tirik"]
#     date_hierarchy = "tugilgan_sana"




class KitobAdmin(admin.ModelAdmin):
    list_display = ["id","nom", "janr", "sahifa","muallif"]
    list_display_links = ["nom"]
    list_editable = ["sahifa"]
    search_fields = ["nom","id" , "muallif__ism"]
    list_filter = ["janr","muallif"]
    autocomplete_fields = ["muallif"]

"1 masala"

class KutubxonachiAdmin(admin.ModelAdmin):
    list_display = ["id","ism","ish_vaqti"]
    search_fields = ["ism"]
    list_filter = ["ish_vaqti"]
    search_help_text = "ish vaqti boyicha qidiruv"


"2 masala"

class MuallifAdmin(admin.ModelAdmin):
    list_display = ["id","ism", "jins", "tugilgan_sana","kitoblar_soni","tirik"]
    list_display_links = ["id","ism"]
    list_editable = ["kitoblar_soni","tirik"]
    search_fields = ["ism","id"]
    search_help_text = "ismi boyicha qidirush"
    list_filter = ["tirik"]
    date_hierarchy = "tugilgan_sana"

"3 masala"

class RecordAdmin(admin.ModelAdmin):
    list_display = ["id","talaba","kitob","kutubxonachi","olinagan_sana","qaytardi","qaytarish_sana"]
    list_editable = ["talaba","kitob","kutubxonachi","olinagan_sana","qaytardi","qaytarish_sana"]
    autocomplete_fields = ["talaba","kitob","kutubxonachi"]
    search_fields = ["talaba__ism","kitob__nom","kutubxonachi__ism"]
    search_help_text = "Qidirish"
    date_hierarchy = "olinagan_sana"


admin.site.register(Talaba,TalabaAdmin)
admin.site.register(Muallif, MuallifAdmin)
admin.site.register(Kitob,KitobAdmin)
admin.site.register(Kutubxonachi, KutubxonachiAdmin)
admin.site.register(Record,RecordAdmin)




