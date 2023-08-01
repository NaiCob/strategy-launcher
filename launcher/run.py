import importlib
import sys

from context import Context


if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        print(f"Arguments: {sys.argv = }")
        template_type: str = sys.argv[1] if sys.argv in ["a", "b"] else "default"
        print()

        m = importlib.import_module(f"templates.template_{template_type}.template")

        context = Context(m.Template())
        print(f"Client: Strategy is set to strategy '{sys.argv[1]}'.")
        print(context.load_excel_file())
        print()

    else:
        print("Strategy not selected")

    print()
    print("DONE")