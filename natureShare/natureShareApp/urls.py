from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('success', success, name = 'success'),
    path('organism_images', views.display_images, name = 'organism_images'),
    # path('detail/<int:pk>', views.detail_view, name='detail_view'),
    path('<int:pk>', views.OrganismDetailView.as_view(), name='organism-detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)