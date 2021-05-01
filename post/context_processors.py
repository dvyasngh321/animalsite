from .models import Category


def footer_categories(request):
	footer_categories = Category.objects.filter(is_active=True).order_by('-is_featured')[:5]

	return {'footer_categories': footer_categories}
