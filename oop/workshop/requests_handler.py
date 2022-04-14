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
from bs4 import BeautifulSoup


class UnsuccessfulNewsRequest(ConnectionError):
    def __init__(self, base_url, url):
        super().__init__("UnsuccessfulNewsRequest error")
        self.base_url = base_url
        self.url = url

    def get_not_responding_url(self):
        return (
            f"Base url ({self.base_url}) (server) seems to be inactive"
            f" when trying to reach {self.url}"
        )


class RequestsHandler:
    BASE_URL = f"http://0.0.0.0:7300"
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

    def get_news_content(self, news_ulr):
        factor_rates = {}

        try:
            try:
                response = requests.get(urljoin(self.BASE_URL, news_ulr), timeout=3)
            except:
                raise UnsuccessfulNewsRequest(self.BASE_URL, news_ulr)
        except UnsuccessfulNewsRequest as ex:
            print(ex.get_not_responding_url())
            return factor_rates

        response.raise_for_status()

        # if response.status_code == 200:
        #     print(response.text)

        parsed = BeautifulSoup(response.text, "html.parser")
        rates = parsed.findAll("span", attrs={"class": "rate"})
        for r in rates:
            factor_name = " ".join(r.parent.text.split(" ")[:-1])
            factor_rates[factor_name] = r.text
        return factor_rates

    def get_news_factors(self):
        news_factor_rates = {}
        for url in ["/frog-news", "/wolf-news", "/eagle-news"]:
            news_factor_rates[url[1:]] = self.get_news_content(url)
        return news_factor_rates
