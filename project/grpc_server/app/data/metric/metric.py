from datetime import datetime
from typing import List
from data.metric.data_point import DataPoint
from data.data_loader.base import DataLoader

class Metric:
    def __init__(self, data_loader: DataLoader):
        self.data_loader = data_loader

    def get_data_between(self, start_time: datetime, end_time: datetime) -> List[DataPoint]:
        data_points = self.data_loader.get_data_between(start_time, end_time)
        return data_points
