from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import ContactViewSet, MailingViewSet, MessageViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('contacts', ContactViewSet)
router_v1.register('mailings', MailingViewSet)
router_v1.register('messages', MessageViewSet)

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router_v1.urls))
]
