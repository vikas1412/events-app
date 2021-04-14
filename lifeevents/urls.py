from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('events/', include('event.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', RedirectView.as_view(url="events/", permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_type=settings.STATIC_ROOT)
