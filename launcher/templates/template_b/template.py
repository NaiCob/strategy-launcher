import importlib
from datetime import date

import common.template as common
from strategy import Strategy


class Template(Strategy):

    def __init__(self) -> None:
        super().__init__()

        common = importlib.import_module("common.config")
        config = importlib.import_module("templates.template_b.config")

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
        return "Template B!"


    def get_client_mapping(self) -> dict:
        pass


    def get_assortment_mapping(self) -> dict:
        pass


    def apply_transformtion(self):
        "No additional transformation"
        pass


    def add_standard_columns(self):
        pass


    def compute_standard_columns(self):
        pass


    def add_month_column(self):
        pass


    def add_distributor_column(self):
        pass


    def clean_nip_number(self):
        pass


    def save_as_csv(self):
        file_name: str = f'{self.config.get("output_file_name")}_{date.today().strftime("%d_%m_%Y")}'

        path_to_output_file = common.get_path_to_file(
            self.config.get("output_folder_path"),
            file_name,
            self.config.get("output_file_extension"),
        )
        
        common.save_as_csv(self._dataframe, path_to_output_file)
        return self._dataframe
