import importlib
import logging
import os
import sys

from common.config import config
from context import Context
from logger.config import init_logging
from utils.decorators import log

init_logging()
logger = logging.getLogger("launcher")

class Launcher:

    @staticmethod
    def get_available_files() -> list:
        return [
            file_name.split(".")[0]
            for file_name 
            in os.listdir(config.get("input_folder_path", None))
        ]


    @staticmethod
    def get_available_modules() -> list:
        return [
            file_name.split("_")[-1]
            for file_name 
            in os.listdir("templates")
        ]


    @log
    def run(self, job_id: str, start_date: str, template_type: str) -> None:
            assert template_type in Launcher.get_available_files()
            assert template_type in Launcher.get_available_modules()

            m = importlib.import_module(f"templates.template_{template_type}.template")

            context = Context(m.Template(job_id, start_date))
            logger.info(f"Start process for template '{template_type}'.")

            logger.info("Transformations to 'bronze' layer started...")
            context.load_excel_file()
            context.save_as_csv("bronze")
            logger.info("Transformations to 'bronze' layer ended...")

            logger.info("Transformations to 'silver' layer started...")
            context.load_csv_file("bronze")
            context.get_mapping("client_mapping")
            context.get_mapping("assortment_mapping")
            context.apply_transformation()
            context.add_standard_columns()
            context.compute_standard_columns()
            context.add_const_column("Miesiąc", "month_year")
            context.add_const_column("Dystrybutor", "distributor_name")
            context.remove_non_numeric("nip_number_column_name")
            context.save_as_csv("silver")
            logger.info("Transformations to 'silver' layer ended...")


            logger.info("Transformations to 'gold' layer started...")
            context.load_csv_file("silver")
            context.save_as_csv("gold")
            logger.info("Transformations to 'gold' layer ended...")

            logger.info(f"End process for template '{template_type}'.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        job_id, start_date, template_type = sys.argv[1], sys.argv[2], sys.argv[3]
        logger.info(f"Parameters: {job_id = }, {start_date = }, {template_type = }.")
        
        Launcher().run(job_id, start_date, template_type)
    else:
        logger.info(Launcher.get_available_files())
        logger.info("#TODO - run all")