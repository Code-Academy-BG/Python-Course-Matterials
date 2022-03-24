from oop.design_patterns.creational.factories import factory
from oop.design_patterns.creational.serializers.serializers import JsonSerializer, XmlSerializer
from oop.design_patterns.creational.serializers.serializers_demo import SongSerializer
from oop.design_patterns.creational.serializers.songs import Song

song = Song('1', 'Water of Love', 'Dire Straits')
serializer = SongSerializer()

print(serializer.serialize(song, 'JSON'))
print(serializer.serialize(song, 'XML'))
print(serializer.serialize(song, 'YAML'))


# Using factory
factory.register_serializer("JSON", JsonSerializer)
factory.register_serializer("XML", XmlSerializer)


class ObjectSerializer:
    def serialize(self, serializable, format):
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()


song = Song("15", "We will rock you", "Queen")
obj_serializer = ObjectSerializer()
print(obj_serializer.serialize(song, "XML"))
print(obj_serializer.serialize(song, "JSON"))
