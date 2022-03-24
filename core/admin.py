from django.contrib import admin
from .models import Publisher,Author,Book,Message

class PublisherAdmin(admin.ModelAdmin):
	list_display = ['name','reg_no']
	list_filter = ['name','reg_no']

class AuthorAdmin(admin.ModelAdmin):
	list_display = ['firstname','lastname','date_of_birth']

class BookAdmin(admin.ModelAdmin):
	list_display = ['title','publisher','year_published','size']
	list_filter = ['title','author','publisher']
	search_fields = ['title','author','publisher']

admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)

admin.site.register(Message)