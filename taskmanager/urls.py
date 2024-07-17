from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('api/users/', include('users.urls')),
    path('api/members/', include('member.urls')),
    path('', RedirectView.as_view(url='/admin/', permanent=False)),  # Redirect root to admin
]
