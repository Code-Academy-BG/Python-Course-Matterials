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
import django.core.management.commands.runserver as runserver

import requests


class RequestsHandler:
    cmd = runserver.Command()
    BASE_URL = f"http://127.0.0.1:{cmd.default_port}"
    FILES_URL = "oop/api/orders/files"
    FILE_URL = "oop/api/orders/file"

    def get_files(self):
        response = requests.get(urljoin(self.BASE_URL, self.FILES_URL), timeout=3)
        response.raise_for_status()
        return response.json()

    def get_file(self, filename):
        json = {
            "file": filename,
        }
        response = requests.get(urljoin(self.BASE_URL, self.FILE_URL), timeout=3, json=json)
        response.raise_for_status()

        yield response.json()["results"]

        next_page = response.json()["next"]
        while next_page:
            next_response = requests.get(next_page, timeout=3, json=json)
            next_response.raise_for_status()
            next_page = next_response.json()["next"]
            yield next_response.json()["results"]

