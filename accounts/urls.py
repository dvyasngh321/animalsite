from django.contrib.auth import views as auth_views
from django.urls import path

from .import views

urlpatterns = [
	path('signup/', views.register, name="register"),
	path('profile/', views.profile_view, name='profile'),

	path('login/', views.login_view, name="login"),
	path('logout/', views.logout_view, name="logout"),
	path('profile/update/', views.profile_form, name="profile_update"),

	# using default auth view for pasword change and reset
	path('change_password/', auth_views.PasswordChangeView.as_view()),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
	path('password_reset/', auth_views.PasswordResetView.as_view()),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/',
		auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
