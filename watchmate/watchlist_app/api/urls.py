from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import WatchListView, WatchDetailView, StreamingPlatformViewSet, ReviewListView, ReviewDetailView

router = DefaultRouter()
router.register('streaming', StreamingPlatformViewSet, basename='streaming')

urlpatterns = [
    path('list/', WatchListView.as_view(), name='watch-list'),
    path('<int:pk>', WatchDetailView.as_view(), name='watch-detail'),
    path('', include(router.urls)),
    path('<int:pk>/reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),
]
