from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import WatchListViewSet, StreamingPlatformViewSet, ReviewListView, ReviewDetailView

router = DefaultRouter()
router.register('streaming', StreamingPlatformViewSet, basename='streaming')
router.register('list', WatchListViewSet, basename='watch')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),
]
