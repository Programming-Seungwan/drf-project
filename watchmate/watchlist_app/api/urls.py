from django.urls import path
from watchlist_app.api.views import WatchListView, WatchDetailView, StreamingListView, StreamingDetailView, ReviewListView, ReviewDetailView


urlpatterns = [
    path('list/', WatchListView.as_view(), name='watch-list'),
    path('<int:pk>', WatchDetailView.as_view(), name='watch-detail'),
    path('streaming/', StreamingListView.as_view(), name = 'streaming'),
    path('streaming/<int:pk>', StreamingDetailView.as_view(), name = 'streaming-detail'),
    path('<int:pk>/reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),
]
