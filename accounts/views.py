from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from post.models import Post
from .models import Profile
from .forms import LoginForm, ProfileForm, UserForm


def register(request):
    if request.user.is_authenticated:
    	return redirect('home')
    form = UserForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.info(request, "created successfully")
            return redirect('login')
        print(form.errors)
        messages.error(request, "Something is wrong!")
    return render(request, 'accounts/register.html', {'form':form})



def login_view(request):
	if request.user.is_authenticated:
		return redirect('/')
	form = LoginForm(request.POST or None)
	if request.method == 'POST':
		print("a")
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect(request.GET.get('next', '/'))
		print(form.errors)
		messages.error(request, 'Invalid login credentials!')
	return render(request, 'accounts/login.html', {'forms': form})


def logout_view(request):
	logout(request)
	return redirect('/')



@login_required
def profile_view(request):
	deac_id = request.GET.get('deactivate')
	if deac_id:
		try:
			post = Post.objects.get(id=deac_id)
		except Exception as e:
			print('Exception: {}'.format(e))
		else:
			post.is_active = False
			post.save()
		return redirect('profile')
	posts = Post.objects.filter(posted_by=request.user).order_by('-is_active', '-created_date')
	return render(request, 'accounts/profile.html', {'posts': posts})


def profile_form(request):
    p_form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, "Updated Successfully!")
            return redirect('home')
        else:
            p_form = ProfileForm(instance=request.user.profile)
    context = {'p_form': p_form}
    return render(request, 'accounts/profile_update.html', context)


