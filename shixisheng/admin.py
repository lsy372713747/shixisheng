from django.contrib import admin
from .models import tImage,Text,Index,GoodStudent,Item,Company,Student,Image

class tImageInfoAdmin(admin.ModelAdmin):
	list_display = ('id',"name",)
class TextInfoAdmin(admin.ModelAdmin):
	list_display = ('id',"test","txt")
class ImageInfoAdmin(admin.ModelAdmin):
	list_display = ('id','img')


class IndexInfoAdmin(admin.ModelAdmin):
	list_display = ('id',"name",)
class ItemInfoAdmin(admin.ModelAdmin):
	list_display = ('id',"name",)	
class GoodStudentInfoAdmin(admin.ModelAdmin):
	list_display = ('id',"name",)


class CompanyInfoAdmin(admin.ModelAdmin):
	list_display = ('id',"name",)

class StudentInfoAdmin(admin.ModelAdmin):
	list_display = ('id',"name",)

admin.site.register(tImage,tImageInfoAdmin)
admin.site.register(Text,TextInfoAdmin)
admin.site.register(Image,ImageInfoAdmin)

admin.site.register(Index,IndexInfoAdmin)
admin.site.register(Item,ItemInfoAdmin)

admin.site.register(GoodStudent,StudentInfoAdmin)

admin.site.register(Company,CompanyInfoAdmin)

admin.site.register(Student,StudentInfoAdmin)

