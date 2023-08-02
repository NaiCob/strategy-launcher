import importlib
import sys

from context import Context


if __name__ == "__main__":
    
    if len(sys.argv) > 1 and sys.argv[1] in ['a', 'b']:
        print(f"Arguments: {sys.argv = }")
        print()
         
        m = importlib.import_module(f"strategies.concrete_strategy_{sys.argv[1]}")
    
        context = Context(m.ConcreteStrategy())
        print(f"Client: Strategy is set to strategy '{sys.argv[1]}'.")
        context.do_some_business_logic()
        print()

    else:
        print("Strategy not selected")

    print()
    print("DONE")
