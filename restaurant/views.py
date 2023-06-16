from rest_framework import viewsets, permissions, generics, status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiResponse
from drf_spectacular.types import OpenApiTypes

from .models import Restaurant, Table, Reservation
from .serializers import RestaurantSerializer, RestaurantDetailSerializer, TableSerializer, TableDetailSerializer, \
    PublicReservationSerializer, ReservationSerializer


class RestaurantListView(generics.ListAPIView):
    """
    Get a list of all restaurants.
    """
    queryset = Restaurant.objects.all().order_by("name")
    serializer_class = RestaurantDetailSerializer


class RestaurantDetailView(generics.RetrieveAPIView):
    """
    Get details for a restaurant.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer


class TableListView(generics.ListAPIView):
    """
    View all tables of the input restaurant.
    """
    serializer_class = TableSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Table.objects.filter(restaurant_id=self.kwargs["pk"])


class TableDetailView(generics.RetrieveAPIView):
    """
    API endpoint to get details for a table.

    Allows to view the Active reservations for the table.

    """
    queryset = Table.objects.all()
    serializer_class = TableDetailSerializer
    permission_classes = [permissions.AllowAny]


class ReservationViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    """
    ViewSet for users to view make, and manage their reservations.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReservationSerializer

    def get_queryset(self):
        return Reservation.objects.filter(customer=self.request.user)

    # GET Operations
    @extend_schema(
        operation_id="reservation_list_active",
    )
    @action(detail=False, methods=["get"], name="List active reservations")
    def list_active(self, request):
        """
        Get all active reservations of the user.

        """
        queryset = self.get_queryset().filter(state=Reservation.State.ACTIVE)
        serializer = self.get_serializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    # Modifying Operations
    @extend_schema(
        operation_id="make_reservation",
    )
    @action(detail=False, methods=["post"], name="Reserve Table")
    def reserve(self, request):
        """
        Reserve a table.

        NOT IMPLEMENTED:
        Not allowed if the table is already reserved in this time.

        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        # TODO Validatate that table is available in this time
        serializer.save(customer=self.request.user.customer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        operation_id="reservation_cancel",
    )
    @action(detail=True, methods=["delete"], name="Cancel Reservation")
    def cancel(self, request, pk=None, format=None):
        """
        Cancel a reservation. (NOT IMPLEMENTED)

        NOT IMPLEMENTED:
        Only possible if the reservation is Active
        and the user is the owner of the reservation.

        """
        reservation = self.get_object()
        # TODO Implement canceling
        return Response(status=status.HTTP_205_RESET_CONTENT)


class TeapotView(APIView):
    """
    Teapot
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = None

    @extend_schema(
        operation_id="teapot",
        request=None,
        responses={418: OpenApiTypes.STR},
    )
    def get(self, request, format=None):
        return Response("I'm a teapot", status=status.HTTP_418_IM_A_TEAPOT)
