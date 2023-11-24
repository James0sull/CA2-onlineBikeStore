from django.urls import path
from .views import SearchResultsListView

app_name='searchApp'

urlpatterns = [
 path('', SearchResultsListView.as_view(), name='searchResult'),
]