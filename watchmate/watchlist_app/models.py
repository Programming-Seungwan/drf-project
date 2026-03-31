from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class StreamingPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyLine = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True) # 객체가 생성될때
    update = models.DateTimeField(auto_now=True) # 객체가 저장될 때마다 매번
    active = models.BooleanField(default=True)
    watchList = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return str(self.rating) + " | " + self.watchList.title