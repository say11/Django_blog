from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'post': PostSitemap
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path(r'comments/', include('django_comments_xtd.urls')),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

