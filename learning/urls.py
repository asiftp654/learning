from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("my-cv", include("cv.urls")),
    path("admin", admin.site.urls),
]