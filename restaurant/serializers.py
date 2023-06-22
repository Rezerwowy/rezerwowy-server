from rest_framework import serializers

from restaurant.models import Restaurant, Table, Reservation


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["url", "id",
                  "name", "description"]


class RestaurantDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["url", "id",
                  "name", "layout", "description", "opening_hours", "address", "phone", "email"]


class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Table
        fields = ["url", "id", "capacity", "position_x", "position_y"]


class PublicReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["start", "end"]


class TableDetailSerializer(serializers.HyperlinkedModelSerializer):
    reservations = PublicReservationSerializer(many=True, read_only=True, source="reservation_set")

    class Meta:
        model = Table
        fields = ["url", "id", "restaurant", "capacity", "position_x", "position_y", "reservations"]


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    creation_date = serializers.DateTimeField(read_only=True)
    state = serializers.CharField(read_only=True)

    class Meta:
        model = Reservation
        fields = ["url", "id", "table", "start", "end", "creation_date", "state"]
