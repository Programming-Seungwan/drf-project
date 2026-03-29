from django.urls import path
from watchlist_app.api.views import WatchListView, WatchDetailView, StreamingListView, StreamingDetailView


urlpatterns = [
    path('list/', WatchListView.as_view(), name='watch-list'),
    path('<int:pk>', WatchDetailView.as_view(), name='watch-detail'),
    path('streaming/', StreamingListView.as_view(), name = 'streaming'),
    path('streaming/<int:pk>', StreamingDetailView.as_view(), name = 'streaming-detail')
]
