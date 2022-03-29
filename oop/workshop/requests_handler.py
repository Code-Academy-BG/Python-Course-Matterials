"""
In order to complete the request's handler you'll need to install requirements.txt which
now holds the requests library reference.

You'll need to finish the RequestsHandler class which purpose is to request data from an open
API which currently has two endpoints:

<base_url>:/oop/api/orders/files
Allowed methods - GET
Returns: [filenames]

<base_url>:/oop/api/orders/file
Allowed methods - GET
Params: You need to supply a filename as a JSON data:
{"file": some_file_name}
Returns: File data, paginated. Note that you may need to perform more than one request in order
to get the whole File data!
Think about how to do this in a memory efficient way.

Tips:
- Perform requests and inspect response that the API returns.
- Think about the pagination data
"""
from urllib.parse import urljoin

import requests


class RequestsHandler:
    BASE_URL = "http://4f8c-89-215-235-209.eu.ngrok.io"
    FILES_URL = "oop/api/orders/files"
    FILE_URL = "oop/api/orders/file"



