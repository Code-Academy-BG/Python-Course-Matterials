course = b'Course'
print(course)
# >>> b'Course'

binary_array = bytearray([1, 2, 3])
print(binary_array)
# >>> bytearray(b'\x01\x02\x03')

binary_memoryview = memoryview(course)
print(binary_memoryview)
# >>> <memory at 0x7f1831759700>
