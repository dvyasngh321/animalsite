from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("services/", views.services, name='services'),
    path("contacts/", views.contacts, name='contacts'),
    path("search/", views.search, name='search'),
    path("new-post/", TemplateView.as_view(template_name='post/post-type.html'), name='new-post'),
    path('product/<cat_slug>/', views.product_page, name='product_page'),
    path("product/detail/<pk>/", views.product_detail, name='product_detail'),
    path("post/detail/<pk>/", views.post_detail_view, name='post-detail'),
    path("post/list/<post_type>/", views.post_list_view, name='post-list'),
    path("form/<post_type>/", views.form_view, name='post-form'),
]
