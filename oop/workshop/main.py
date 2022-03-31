import json

from oop.workshop.requests_handler import RequestsHandler

rq = RequestsHandler()
news_factors = rq.get_news_factors()
print(json.dumps(news_factors, indent=4))

"""
{
    "frog_news": {
        "weather": 90%,
        "markets": 5%,
    },
    "wolf_news": {
        "weather": 90%,
        "markets": 5%,
    },
    "eagle_news": {
        "weather": 90%,
        "markets": 5%,
    },
}
"""
