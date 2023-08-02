from abc import ABC, abstractmethod


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def load_excel(self):
        pass

    @abstractmethod
    def get_client_mapping(self):
        pass

    @abstractmethod
    def get_assortment_mapping(self):
        pass

    @abstractmethod
    def apply_transformtion(self):
        pass

    @abstractmethod
    def add_standard_columns(self):
        pass

    @abstractmethod
    def compute_standard_columns(self):
        pass

    @abstractmethod
    def add_month_column(self):
        pass

    @abstractmethod
    def add_distributor_column(self):
        pass

    @abstractmethod
    def clean_nip_number(self):
        pass

    @abstractmethod
    def save_as_csv(self):
        pass
