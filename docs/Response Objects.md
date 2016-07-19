###Response Objects
=========================
If you have this view
``
from news import views

url(r'^archive/$', views.archive, name='news-archive')
``
Then you can use this:
``
# using the named URL
reverse('news-archive')

# passing a callable object
# (This is discouraged because you can't reverse namespaced views this way.)
from news import views
reverse(views.archive)
``
And when you need to use dictionaries :

``
from django.core.urlresolvers import reverse

def myview(request):
    return HttpResponseRedirect(reverse('admin:app_list', kwargs={'app_label': 'auth'}))
``

[Referencia DjangoDocs](https://docs.djangoproject.com/en/1.9/ref/urlresolvers/#django.core.urlresolvers.reverse)
