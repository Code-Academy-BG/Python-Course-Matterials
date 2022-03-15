"""
We can use the direct keyword import to import specific python package within our module.
We can use 'from package import module' which means that we're only importing the needed module
within our program.
The most common error we can face with imports is called 'Cyclic import', which means that we try
to import a module that tries to import a module within our model while the last model is already
imported.
For handling such cases we can use for example 'local imports', which means that we're importing
the package / module we need in the deepest closure of our scope.
"""

import csv
import math
import os
import typing

from collections import OrderedDict, Counter, defaultdict, deque
from decimal import Decimal

from control_flow_and_syntax.input_handle import get_user_age, get_user_details

get_user_age()

get_user_details()
