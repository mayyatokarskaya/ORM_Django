from django.conf import settings  # Добавляем импорт settings
from django.conf.urls.static import static  # Добавляем импорт static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalog.urls")),
    path("blogs/", include("blog.urls", namespace="blog")),
]

# Добавляем обработку медиафайлов только в режиме DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
