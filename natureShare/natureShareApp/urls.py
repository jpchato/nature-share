from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    OrganismDetailView,
    OrganismDelete,
    OrganismUpdate,
    SearchResultsView,
    UserSearchResultsView,
    about,
    display_images,
    home,
    user_organisms,
)

urlpatterns = [
    path('', home, name='home'),
    path('organism_images/', display_images, name='organism_images'),
    path('<int:pk>/', OrganismDetailView.as_view(), name='organism-detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search/user/', UserSearchResultsView.as_view(), name='user_search_results'),
    path('<int:pk>/update/', OrganismUpdate.as_view(), name='edit'),
    path('<int:pk>/delete/', OrganismDelete.as_view(), name='delete'),
    path('user_organisms/', user_organisms, name='user_organisms'),
    path('about/', about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)