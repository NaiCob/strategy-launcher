import importlib

from strategy import Strategy


class Template(Strategy):
    
    def __init__(self) -> None:
        super().__init__()
        
        common = importlib.import_module("common.config")
        config = importlib.import_module("templates.template_a.config")

        self.config = common.config
        self.config.update(config.template_config)


    def load_excel(self) -> str:
        
        print(self.config)
        print()
        
        return "Template A!"
