from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactMessageForm, PostForm
from .models import Category, Post, Product
from accounts.models import Profile

POST_TYPES = {'sell', 'lost', 'found'}


def index(request):
	# add ', is_featured=True' without quoates to show only featured post in home page
	acive_posts = Post.objects.filter(is_active=True)
	lost_pets = acive_posts.filter(post_type='lost')
	found_pets = acive_posts.filter(post_type='found')
	pets_for_sale = acive_posts.filter(post_type='sell', is_featured=True)
	categories = Category.objects.filter(is_active=True).order_by('-is_featured')[:10]
	context = {
			'lost_pets': lost_pets,
			'found_pets': found_pets,
			'pets_for_sale': pets_for_sale,
			'categories': categories}
	return render(request, 'post/index.html', context)


def search(request):
	q = request.GET.get('q')
	posts = Post.objects.filter(Q(description__icontains=q) |
								Q(title__icontains=q))
	return render(request, 'post/list.html', {'posts': posts})
	

def product_page(request, cat_slug):
    categories = Category.objects.all()
    products = Product.objects.all()
    if cat_slug:
        category = get_object_or_404(Category, slug = cat_slug)
        products = products.filter(category = category)
    context = {'category':category , 'products':products, 'categories':categories}
    return render(request, "post/product_page.html", context)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'post/product_detail.html', {'product': product})

def post_list_view(request, post_type):
	if post_type not in POST_TYPES:
		raise Http404
	posts = Post.objects.filter(is_active=True, post_type=post_type)
	return render(request, 'post/list.html', {'posts': posts})


def post_detail_view(request, pk):
	post = get_object_or_404(Post, pk=pk)
	profile = Profile.objects.get(user = post.posted_by)
	related_posts = Post.objects.filter(is_active=True, post_type=post.post_type).exclude(id=post.id)
	return render(request, 'post/detail.html', {'post': post, 'related_posts': related_posts, 'profile': profile})




@login_required
def form_view(request, post_type):
	if post_type not in POST_TYPES:
		raise Http404
	form = PostForm(request.POST or None)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.post_type = post_type
			post.posted_by = request.user
			post.save()
			messages.success(request, "Sucessfully Posted")
			return redirect('post-detail', post.id)
		print(form.errors)
	categories = Category.objects.filter(is_active=True)
	context = {'form': form, 'categories': categories, 'post_type': post_type}
	return render(request, 'post/form.html', context)


def services(request):
	return render(request, 'post/services.html')


def contacts(request):
	form = ContactMessageForm(request.POST or None)
	if request.method == 'POST':
		print(form)
		if form.is_valid():
			form.save()
			messages.success(request, 'Thankyou for your message.')
	return render(request, 'post/contacts.html', {'form': form})
