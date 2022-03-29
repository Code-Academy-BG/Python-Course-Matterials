from oop.workshop.export_builder import OrdersDataExportBuilder


class _LocationData:
    def __init__(self, location):
        self.location = location
        self.products_data = {}

    @property
    def products_count(self):
        return len(self.products_data)


class TimespanOrdersData:
    def __init__(self, filename):
        self.timespan = self.get_timespan_from_filename(filename)
        self.orders = []

    def process_data(self, data_batch):
        self.orders.append(data_batch)

    def get_orders_processor(self):
        return OrdersDataExportBuilder(self.orders, self)

    @property
    def orders_count(self):
        return len(self.orders)

    @staticmethod
    def get_timespan_from_filename(filename):
        return filename.split("_")[-1].split(".")[0]
