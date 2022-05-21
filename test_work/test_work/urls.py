from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from api.views import ContactViewSet, MailingViewSet, MessageViewSet

router_v1 = DefaultRouter()
router_v1.register('contacts', ContactViewSet)
router_v1.register('mailings', MailingViewSet)
router_v1.register('messages', MessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router_v1.urls))
]

schema_view = get_schema_view(
   openapi.Info(
      title="Mailings API",
      default_version='v1',
      description="Документация для API рассылок",
      contact=openapi.Contact(email="admin@malling.api.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
]
