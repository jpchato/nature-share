from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('organism_images', views.display_images, name = 'organism_images'),
    # path('<int:id>', views.detail, name = 'update_organism'),
    path('<int:pk>', views.OrganismDetailView.as_view(), name='organism-detail'),
    # https://learndjango.com/tutorials/django-search-tutorial
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search/', UserSearchResultsView.as_view(), name='user_search_results'),
    path('<pk>/update', OrganismUpdate.as_view(), name='edit'),
    path('<pk>/delete', OrganismDelete.as_view(), name='delete'),
    path('user_organisms', views.user_organisms, name = 'user_organisms'),
    path('about', views.about, name='about')
   
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)