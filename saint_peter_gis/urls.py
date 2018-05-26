"""saint_peter_gis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from accounts import urls as accounts_urls
from blogs import urls as blogs_urls
from events import urls as events_urls
from home.views import get_index,get_contacts,get_faq,get_news,get_events
from django.views.static import serve
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^blogs/', include(blogs_urls)),
    url(r'^events/', include(events_urls)),
    url(r'^$', get_index, name='home'),
    url(r'^contacts', get_contacts, name='contacts'),
    url(r'^faq', get_faq, name='faq'),
    url(r'^news', get_news, name='news'),
    url(r'^events', get_events, name='events'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
