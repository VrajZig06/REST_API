from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("list/",views.list_movies),
    path("list/<int:pk>/",views.movie),
    path("stream/",views.platform_detail),
    path("stream/<int:pk>",views.platform),

]
urlpatterns = format_suffix_patterns(urlpatterns)