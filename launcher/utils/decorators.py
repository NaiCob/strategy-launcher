import functools
import logging
import time
from typing import (
    Any,
    Callable,
)

import pandas as pd


logger = logging.getLogger("transform")


def log(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(*args, **kwargs) -> Any:
        try:
            ts = time.time()
            result = method(*args, **kwargs)
            te = time.time()
            logger.info(f"Processed '{method.__name__}' in {(te - ts):2.2f} seconds.")
            if isinstance(result, pd.DataFrame):
                logger.info(f"DataFrame '{method.__name__}' shape is {result.shape}.")
            return result
        except Exception as e:
            logger.exception(f"Exception raised in '{method.__name__}'. Description: {str(e)}")
            raise e
    return wrapper