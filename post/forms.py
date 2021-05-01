from django import forms

from .models import Post, Category, ContactMessage


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['parent', 'title']


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'category', 'description', 'price', 'location', 'image']


class ContactMessageForm(forms.ModelForm):
	class Meta:
		model = ContactMessage
		fields = ['user', 'name', 'email', 'contact', 'address', 'message']

