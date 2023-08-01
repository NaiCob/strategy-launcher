import importlib

from strategy import Strategy


class Template(Strategy):
    
    def __init__(self) -> None:
        super().__init__()
        
        common = importlib.import_module("common.config")
        config = importlib.import_module("templates.template_default.config")

        self.config = common.config
        self.config.update(config.template_config)


    def load_excel(self) -> str:
        
        print(self.config)
        print()
        
        return "Template DEFAULT!"


    def get_client_mapping(self):
        return super().get_client_mapping()
