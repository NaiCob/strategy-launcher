import importlib
import logging
from typing import Any

import pandas as pd

from strategy import Strategy


logger = logging.getLogger("template_b")


class Template(Strategy):

    def __init__(self, job_id: str, start_date: str, environment: str) -> None:
        super().__init__()
        logger.info("Upload 'template_b' config.")
        common = importlib.import_module("common.config")
        config = importlib.import_module("templates.template_b.config")

        self.config = common.config.get(environment)
        self.config.update(config.template_config)

        self._job_id: str = job_id
        self._start_date: str = start_date
        self._environment = environment


    @property
    def dataframe(self):
        return self._dataframe


    @dataframe.setter
    def dataframe(self, df):
        self._dataframe = df


    def load_excel(self):
        return super().load_excel()


    def load_csv(self, layer_name: str) -> pd.DataFrame:
        return super().load_csv(layer_name)


    def get_mapping(self, mapping_name: str) -> dict:
        return super().get_mapping(mapping_name)


    def apply_transformtion(self):
        "No additional transformation"
        return self._dataframe


    def add_standard_columns(self):
        return super().add_standard_columns()


    def compute_standard_columns(self):
        #TODO - define
        return self._dataframe


    def add_const_column(self, column_name: str, const_value: Any) -> pd.DataFrame:
        return super().add_const_column(column_name, const_value)


    def remove_non_numeric(self, column_name: str) -> None:
        return super().remove_non_numeric(column_name)


    def save_as_csv(self, layer_name: str):
        return super().save_as_csv(layer_name)
