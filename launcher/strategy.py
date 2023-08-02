import os
from abc import (
    ABC,
    abstractmethod,
)
from datetime import date
from typing import Any

import pandas as pd

import common.transformations as common

class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def load_excel(self) -> pd.DataFrame:
        """ Load excel file from input destination defined by template configuration.

        Returns:
            pd.DataFrame: loaded excel file as a dataframe
        """
        path_to_input_file = (
            os
            .path
            .abspath(
                f'{self.config.get("input_folder_path")}/'
                f'{self.config.get("input_file_name")}.'
                f'{self.config.get("input_file_extension")}'
            )
        )

        self._dataframe = (
            pd
            .read_excel(
                path_to_input_file,
                dtype=str,
                skiprows=self.config.get("from_row"),
                sheet_name=self.config.get("sheet_name")
            )
        )
        return self._dataframe


    @abstractmethod
    def get_mapping(self, mapping_name: str) -> pd.DataFrame:
        # self._client_mapping = pd.DataFrame(self.config.get(mapping_name, None))
        # return self._client_mapping
        return self.config.get(mapping_name, None)


    @abstractmethod
    def apply_transformtion(self):
        #TODO - define
        pass


    @abstractmethod
    def add_standard_columns(self):
        for col in self.config.get("standard_columns", []):
            if col not in self._dataframe.columns:
                self._dataframe[col] = None
        return self._dataframe


    @abstractmethod
    def compute_standard_columns(self):
        #TODO - define
        pass

    @abstractmethod
    def add_const_column(self, column_name: str, const_value: Any) -> pd.DataFrame:
        """ Add column with constant value from config to the dataframe.
        If constant value does not exist in config use constant value explicit.
        Drop column first if column already exists.

        Args:
            column_name (str): new column name
            const_value (Any): constant value for new column

        Returns:
            pd.DataFrame: dataframe with new constant column
        """
        self._dataframe.drop(columns=column_name)
        self._dataframe[column_name] = self.config.get(const_value, const_value)
        return self._dataframe


    @abstractmethod
    def remove_non_numeric(self, column_name: str) -> None:
        column: str = self.config.get(column_name)
        self._dataframe[column] = (
            self
            ._dataframe[column]
            .apply(lambda value: "".join(char for char in value if char.isdigit()))
        )


    @abstractmethod
    def save_as_csv(self):
        path = (
            os
            .path
            .abspath(
                f'{self.config.get("output_folder_path")}/'
                f'{self.config.get("output_file_name")}_{date.today().strftime("%d_%m_%Y")}.'
                f'{self.config.get("output_file_extension")}'
            )
        )
        status: bool = True
        try:
            self._dataframe.to_csv(path, header=True, sep=';', encoding='utf-8', index=False)
        except Exception:
            status = False
        return status
