import importlib

from strategy import Strategy
import common.template as common


class Template(Strategy):
    
    def __init__(self) -> None:
        super().__init__()
        
        m = importlib.import_module("templates.template_b.config")
        
        self.config = m.template_config
    
    def load_excel(self) -> str:

        common.common_function("Common function used by template A")
        print(self.config)
        print()
        
        return "Template B!"
