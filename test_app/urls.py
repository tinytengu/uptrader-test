from django.urls import path

from .views import IndexView, AboutView, LinksView

app_name = "test_app"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("links/", LinksView.as_view(), name="links"),
]
