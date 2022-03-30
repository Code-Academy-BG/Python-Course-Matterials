from rest_framework import serializers


class OrderDetailSerializer(serializers.Serializer):
    product = serializers.CharField()
    qty = serializers.DecimalField(max_digits=14, decimal_places=3)
    location = serializers.CharField()
    tolocation = serializers.CharField()


class OrdersSerializer(serializers.Serializer):
    order_id = serializers.SerializerMethodField()
    status = serializers.IntegerField()
    last_update_at = serializers.DateTimeField()
    details = serializers.SerializerMethodField()

    def get_order_id(self, obj):
        return obj["order_id"] // 20 * 355

    def get_details(self, obj):
        return OrderDetailSerializer(obj["details"], many=True).data
