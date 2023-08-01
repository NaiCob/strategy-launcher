import importlib
import sys

from context import Context


if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        print(f"Arguments: {sys.argv = }")
        template_type: str = sys.argv[1] if sys.argv[1] in ["a", "b"] else "default"
        print()

        m = importlib.import_module(f"templates.template_{template_type}.template")

        context = Context(m.Template())
        print(f"Client: Strategy is set to strategy '{sys.argv[1]}'.")
        
        context.load_excel_file()
        context.get_client_mapping()
        context.get_assortment_mapping()
        context.apply_transformation()

        context.add_standard_column()
        context.add_month_column()
        context.add_distributor_column()
        context.clean_nip_number()
        context.save_as_csv()

        print()

    else:
        print("Strategy not selected")

    print()
    print("DONE")