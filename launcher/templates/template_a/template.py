import importlib
from datetime import date

import common.template as common
from strategy import Strategy


class Template(Strategy):
    
    def __init__(self) -> None:
        super().__init__()
        
        common = importlib.import_module("common.config")
        config = importlib.import_module("templates.template_a.config")

        self.config = common.config
        self.config.update(config.template_config)


    @property
    def dataframe(self):
        return self._dataframe


    @dataframe.setter
    def dataframe(self, df):
        self._dataframe = df


    def load_excel(self) -> str:
        print(self.config)
        path_to_input_file = common.get_path_to_file(
                self.config.get("input_folder_path"),
                self.config.get("input_file_name"),
                self.config.get("input_file_extension"),
            )

        self._dataframe = common.read_xlsx_file(
            path=path_to_input_file,
            row=self.config.get("from_row"),
            sheet_name=self.config.get("sheet_name")
        )
        print()
        return "Template A!"


    def get_client_mapping(self) -> dict:
        return self.config.get("client_mapping", None)


    def get_assortment_mapping(self) -> dict:
        return self.config.get("assortment_mapping", None)


    def apply_transformtion(self):
        "No additional transformation"
        return self._dataframe


    def add_standard_columns(self):
        df = common.add_standard_columns(self._dataframe, self.config.get("standard_columns", None))
        self._dataframe = df
        return self._dataframe


    def compute_standard_columns(self):
        #TODO - define
        return self._dataframe


    def add_month_column(self):
        self._dataframe = (
            common
            .add_constant_column(
                self._dataframe,
                "Miesiąc",
                f'{self.config.get("month")}.{self.config.get("year")}'
            )
        )
        return self._dataframe


    def add_distributor_column(self):
        self._dataframe = common.add_constant_column(self._dataframe, "Dystrybutor", self.config.get("distributor_name"))
        return self._dataframe


    def clean_nip_number(self):
        self._dataframe = common.clean_nip_number(self._dataframe, self.config.get("nip_number_column_name", None))
        return self._dataframe


    def save_as_csv(self):
        file_name: str = f'{self.config.get("output_file_name")}_{date.today().strftime("%d_%m_%Y")}'

        path_to_output_file = common.get_path_to_file(
            self.config.get("output_folder_path"),
            file_name,
            self.config.get("output_file_extension"),
        )
        
        common.save_as_csv(self._dataframe, path_to_output_file)
        return self._dataframe
