
from django.contrib.auth.models import User
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class BasicModel(models.Model):
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	is_featured = models.BooleanField(default=False)

	class Meta:
		abstract = True


class Category(BasicModel, MPTTModel):
	"""
	The category of the pet for filtering
	"""
	parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
	title = models.CharField(max_length=100)
	slug = models.SlugField()

	def __str__(self):
		return self.title 

	def get_absolute_url(self):
		return f"/{self.slug}/"


class Product(BasicModel):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images/category/', null=True, blank=True)
	description = models.TextField()

	def __str__(self):
		return self.title	


class Post(BasicModel):
	TYPE_CHOICES = [('lost', 'Lost'), ('found', 'Found'), ('sell', 'Sell')]
	post_type = models.CharField(max_length=5, choices=TYPE_CHOICES)

	posted_by = models.ForeignKey(User, related_name='posts', on_delete=models.SET_NULL,
									null=True, blank=True)
	# user who
	closed_to = models.ForeignKey(User, related_name='closed_posts', on_delete=models.SET_NULL,
									null=True, blank=True)

	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=100, blank=True)
	code = models.CharField(max_length=15, unique=True)
	description = models.TextField()
	price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
	location = models.CharField(max_length=255)
	image = models.ImageField(upload_to='images/site/', null=True, blank=True)

	def __str__(self):
		return '{}-{}'.format(self.post_type, self.id)

	def save(self, *args, **kwargs):
		if self.id is None:
			super().save(*args, **kwargs)
		code = '{}-{}'.format(self.post_type, self.id)
		self.code = code
		super().save(*args, **kwargs)


class PostReactions(BasicModel):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	description = models.TextField()
	seen = models.BooleanField(default=False)


class ContactMessage(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	name = models.CharField(max_length=255)
	email = models.EmailField()
	contact = models.CharField(max_length=20)
	address = models.CharField(max_length=255, blank=True)
	message = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{}-{}'.format(self.id, self.name)
