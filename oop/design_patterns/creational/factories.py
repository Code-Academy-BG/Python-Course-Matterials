class SerializersFactory:
    def __init__(self):
        self._serializers = {}

    def register_serializer(self, format, serializer):
        if format in self._serializers:
            return "Serializers factory already have this serializer"
        self._serializers[format] = serializer

    def get_serializer(self, format):
        if not self._serializers.get(format):
            raise TypeError("Not existing serializer wanted")
        return self._serializers[format]()


factory = SerializersFactory()
