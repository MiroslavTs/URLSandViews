from django.urls import path, re_path, include

from urlsAndViews.departments import views
from urlsAndViews.departments.views import index

urlpatterns = [
    path('', views.index, name='home'),
    path('redirect/', views.redirect_to_view),
    path('softuni/', views.redirect_to_softuni),
    path('numbers/', include([
        path('<int:pk>/', views.view_with_int_pk),
        path('<int:pk>/<slug:slug>/', views.view_with_slug),
    ])),
    path('<variable>/', views.view_with_name),
    re_path(r'^archive/(?P<archive_year>202[0-3])/$', views.show_archive),
    path('<path:variable>', views.view_with_name),
]
