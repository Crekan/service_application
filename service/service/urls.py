from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from services.views import SubscriptionView

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

router = routers.DefaultRouter()
router.register(r'api/subscriptions', SubscriptionView)
urlpatterns += router.urls
