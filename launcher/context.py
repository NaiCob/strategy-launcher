from strategy import Strategy


class Context():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy


    def load_excel_file(self) -> None:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """
        return self._strategy.load_excel()

        
    def get_client_mapping(self) -> None:
        return self._strategy.get_client_mapping()


    def get_assortment_mapping(self) -> None:
        return self._strategy.get_assortment_mapping()


    def apply_transformation(self) -> None:
        return self._strategy.apply_transformtion()


    def add_standard_column(self) -> None:
        return self._strategy.add_standard_column()


    def add_month_column(self) -> None:
        return self._strategy.add_month_column()


    def add_distributor_column(self) -> None:
        return self._strategy.add_distributor_column()


    def clean_nip_number(self) -> None:
        return self._strategy.clean_nip_number()


    def save_as_csv(self) -> None:
        return self._strategy.save_as_csv()
    