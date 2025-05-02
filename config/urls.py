from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalog.urls", namespace="catalog/")),
]



from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Добавляем импорт settings
from django.conf.urls.static import static  # Добавляем импорт static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalog.urls", namespace="catalog")),  # Убрал слеш в namespace
]

# Добавляем обработку медиафайлов только в режиме DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)