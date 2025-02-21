from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


# Functional Based View 
# urlpatterns = [
#     path("list/",views.list_movies),
#     path("list/<int:pk>/",views.movie),
#     path("stream/",views.platform_detail),
#     path("stream/<int:pk>",views.platform),
# ]

# Class Based View

urlpatterns = [
    path('movies/',views.list_movies,name="movie-list"),
    path('movie/<int:pk>/',views.movie),
    path('platforms/',views.StreamPlatformList.as_view(),name='platform-list'),
    path('platforms/<int:pk>/',views.StreamPlatformDetails.as_view()),
    path('',views.api_root)
]


urlpatterns = format_suffix_patterns(urlpatterns)