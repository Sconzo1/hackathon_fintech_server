from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

import spectacular.auth_extensions

# Чтобы IDE не ругалась на пустой import. Зачем пустой? Чтобы подгружалась custom авторизация в swagger
fish = spectacular.auth_extensions.KnoxTokenScheme

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
