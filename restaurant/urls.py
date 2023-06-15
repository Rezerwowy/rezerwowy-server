from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r"reservation", views.ReservationViewSet, basename="reservation")

urlpatterns = [
    path("restaurant/", views.RestaurantListView.as_view(), name="restaurant-list"),
    path("restaurant/<int:pk>/", views.RestaurantDetailView.as_view(), name="restaurant-detail"),
    path("restaurant/<int:pk>/tables/", views.TableListView.as_view(), name="table-list"),
    path("table/<int:pk>/", views.TableDetailView.as_view(), name="table-detail"),

    path("", include(router.urls)),

    path("teapot/", views.TeapotView.as_view(), name="teapot"),
]
