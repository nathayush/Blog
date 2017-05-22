from django.conf.urls import url

from . import views

#urls are declared here
urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^view/(?P<slug>[^\.]+).html', views.view_post, name='view_blog_post'),
	url(r'^category/(?P<slug>[^\.]+).html', views.view_category, name='view_blog_category'),
	url(r'^add_post.html', views.add_post, name='add_post'),
	url(r'^submit.html', views.submit, name='submit'),
	url(r'^get_price.html', views.get_price, name='get_price'),
]
