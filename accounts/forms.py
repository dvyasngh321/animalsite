from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):

	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'email')

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
			return password2

	def clean_username(self):
		return self.cleaned_data.get("username").lower()

	def clean_email(self):
		return self.cleaned_data.get("email").lower()

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data.get("password1"))
		if commit:
			user.save()
		return user


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

	def clean_username(self):
		return self.cleaned_data.get("username").lower()

	class Meta:
		fields = ('email','password')


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['name', 'contact','photo']
