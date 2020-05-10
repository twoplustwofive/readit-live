from django.conf.urls import url
from .import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'Blog'
urlpatterns = [
    path('',views.home,name='home'),
    path('<slug:slug>/<int:id>',views.article_details,name="article_details"),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('write',views.write,name='write'),
]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
