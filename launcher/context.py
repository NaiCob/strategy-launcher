from strategy import Strategy


class Context():

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy


    def load_excel_file(self) -> None:
        return self._strategy.load_excel()

        
    def get_client_mapping(self) -> None:
        return self._strategy.get_client_mapping()


    def get_assortment_mapping(self) -> None:
        return self._strategy.get_assortment_mapping()


    def apply_transformation(self) -> None:
        return self._strategy.apply_transformtion()


    def add_standard_columns(self) -> None:
        return self._strategy.add_standard_columns()


    def compute_standard_columns(self) -> None:
        return self._strategy.compute_standard_columns()


    def add_month_column(self) -> None:
        return self._strategy.add_month_column()


    def add_distributor_column(self) -> None:
        return self._strategy.add_distributor_column()


    def clean_nip_number(self) -> None:
        return self._strategy.clean_nip_number()


    def save_as_csv(self) -> None:
        return self._strategy.save_as_csv()
    