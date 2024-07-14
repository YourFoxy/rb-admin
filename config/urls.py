from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from apps.books.views import BookViewSet, CriterionViewSet, ProvenentionViewSet
from apps.libraries.views import LibraryTypeViewSet, LibraryViewSet
from apps.series.views import SeriesViewSet

libraries_router = DefaultRouter()
libraries_router.register("types", LibraryTypeViewSet)
libraries_router.register("", LibraryViewSet)

books_router = DefaultRouter()
books_router.register("criteria", CriterionViewSet)
books_router.register("provenentions", ProvenentionViewSet)
books_router.register("", BookViewSet)

api_v1_urlpatterns = [
    path("health-check/", lambda req: JsonResponse({"status": "working"})),
    path("libraries/", include(libraries_router.urls)),
    path("books/", include(books_router.urls)),
    path("series/", SeriesViewSet.as_view({"get": "list"})),
]

api_urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("v1/", include(api_v1_urlpatterns)),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_urlpatterns)),
    path("", lambda req: HttpResponse("Library catalog")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
