from django.contrib import admin
from addressbook import models
# Register your models here.

admin.site.register(models.Book)

class BookAdmin(admin.ModelAdmin):
    fields = ('id','name','email','phone')
    list_filter = ('name', )
    search_fields = ('email','name')