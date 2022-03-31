from oop.workshop.orders_data import TimespanOrdersData
from oop.workshop.requests_handler import RequestsHandler

rq = RequestsHandler()
files = rq.get_files()

timespan_handler = TimespanOrdersData(files[0])
for results in rq.get_file(files[0]):
    for order_data in results:
        timespan_handler.process_data(order_data)

orders_processor = timespan_handler.get_orders_processor()
orders_processor.export_grouped_by_location("xml", "location")
