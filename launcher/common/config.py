config: dict = {
    "dev": {
        "input_folder_path": "local_data/input",
        "input_file_name": "dummy",
        "input_file_extension": "xlsx",
        "bronze_folder_path": "local_data/bronze",
        "silver_folder_path": "local_data/silver",
        "gold_folder_path": "local_data/gold",
        "output_file_name": "dummy",
        "output_file_extension": "csv",
        "from_row": 0,
        "sheet_name": "Sheet1",
        "standard_columns": [
            "Wartość netto",
            "Ilość_szt",
            "Miesiąc",
            "Dystrybutor",
            "ID_Pomocnicze_Asortyment",
            "ID_Pomocnicze_Klient",
            "Spółka",
            "D. Wst.",
            "D. Wyst.",
            "Cena",
            "Pozycja",
            "SR"
        ],
        "month_year": "05.2023",
    }
}