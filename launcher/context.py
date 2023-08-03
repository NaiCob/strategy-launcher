
from typing import Any

from strategy import Strategy
from utils.decorators import log


class Context():

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @log
    def load_excel_file(self) -> None:
        return self._strategy.load_excel()
    
    
    @log
    def load_csv_file(self, layer_name: str) -> None:
        return self._strategy.load_csv(layer_name)


    @log
    def get_mapping(self, mapping_name: str) -> None:
        return self._strategy.get_mapping(mapping_name)


    @log
    def apply_transformation(self) -> None:
        return self._strategy.apply_transformtion()


    @log
    def add_standard_columns(self) -> None:
        return self._strategy.add_standard_columns()


    @log
    def compute_standard_columns(self) -> None:
        return self._strategy.compute_standard_columns()


    @log
    def add_const_column(self, column_name: str, const_value: Any) -> None:
        return self._strategy.add_const_column(column_name, const_value)


    @log
    def remove_non_numeric(self, column_name: str) -> None:
        return self._strategy.remove_non_numeric(column_name)


    @log
    def save_as_csv(self, layer_name: str) -> None:
        return self._strategy.save_as_csv(layer_name)
