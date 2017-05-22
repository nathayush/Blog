from moneywagon import get_current_price
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from .models import Blog, Category

# Create your views here.

def index(request):
	return render(request, 'index.html', {
		'categories': Category.objects.all(),
		'posts': Blog.objects.all().order_by('posted').reverse()[:5]
	})

def view_post(request, slug):   
    return render(request, 'view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)
    })
    
def add_post(request):
	return render(request, 'add_post.html')

def submit(request):
	title1 = request.POST.get('title', '')
	category1 = request.POST.get('category', '')
	body1 = request.POST.get('body', '')
	slug1 = request.POST.get('slug', '')
#	obj1 = Category.objects.create(title=category1)
	if Category.objects.filter(title = category1).exists():
		category = Category.objects.get(title=category1, slug=slugify(category1))
		newpost = Blog.objects.create(title=title1, category=category, body=body1, slug=slug1)
		print(slugify(title1))
#		obj = Blog.objects.create(title=title1, category=category1, body=body1)
	else:
		category = Category.objects.create(title=category1, slug=slugify(category1))
		newpost = Blog.objects.create(title=title1, category=category, body=body1, slug=slug1)
#		obj1 = Category.objects.create(title=category1)
#		obj2 = Blog.objects.create(title=title1, category=category1, body=body1)
	return render(request, 'submit.html')

def get_price(request):
	price_btc = get_current_price('btc', 'usd')
	price_eth = get_current_price('eth', 'usd')
	return render(request, 'get_price.html', {
		'price_btc': price_btc,
		'price_eth': price_eth
	})
