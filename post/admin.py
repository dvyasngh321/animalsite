from django.contrib import admin
from .models import Category,Product, ContactMessage, Post

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title']

class ProductAdmin(admin.ModelAdmin):
	list_display = ['title', 'category']

class PostAdmin(admin.ModelAdmin):
	list_display = ['category', 'code']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(ContactMessage)
