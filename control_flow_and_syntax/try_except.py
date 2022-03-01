import traceback


class CodeAcademyException(Exception):
    pass


# if 5 < 6:
#     raise CodeAcademyException('Raised CodeAcademyException')


try:
    5 / 0
except ZeroDivisionError:
    print("Raised zero division error")
