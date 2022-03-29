import csv
import itertools


class OrdersDataExportBuilder:
    ALLOWED_GROUPERS = {"location", "product"}

    def __init__(self, data, timespan_orders_holder):
        self.fetched_data = data
        self.timespan_orders_holder = timespan_orders_holder

    def export_as_csv(self, group_by):
        pass

    def export_as_xml(self, group_by):
        pass

    def export_grouped_by_location(self, format, group_by):
        if group_by not in self.ALLOWED_GROUPERS:
            raise ValueError(f"Unknown grouping element: {group_by}")

        if format == "csv":
            self.export_as_csv(group_by)
        elif format == "xml":
            self.export_as_xml(group_by)
        else:
            raise ValueError(f"Unknown format: {format}")
