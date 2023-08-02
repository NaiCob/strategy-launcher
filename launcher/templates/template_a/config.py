template_config: dict = {
    "input_file_name": "a",
    "input_file_extension": "xlsx",
    "output_file_name": "a",
    "output_file_extension": "csv",
    "from_row": 0,
    "sheet_name": "Sheet1",
    "client_mapping": {
        "ID_Pomocnicze_Klient": [
            "Kod odbiorcy sklepu",
            "Nazwa sklepu",
            "Miejscowość",
            "Adres",
            "NIP",
        ],
        "dane_klient_join_col": "ID_Pomocnicze_Klient",
        "klient_join_col": "ID_Weryf.",
        "kolumny_do_dodania": [
            "ID",
            "ID_Weryf.",
        ]
    },
    "assortment_mapping": {
        "ID_Pomocnicze_Asortyment": "",
        "dane_asortyment_join_col": "Nazwa produktu",
        "asortyment_join_col": "Nazwa produktu",
        "asortyment_kolumny_do_dodania": [
            "Przelicznik (szt)",
            "ID Info",
            "Nazwa MW",
            "Nazwa produktu",
        ],
    },
    "distributor_name": "ALERT",
    "month_year": "05.2023",
    "nip_number_column_name": "NIP",
}