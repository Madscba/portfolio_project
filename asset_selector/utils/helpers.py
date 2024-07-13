"""Script containing helper functions."""
import datetime
import functools
import logging
import os
import re
import time
from pathlib import Path

import colorlog
import pandas as pd

from asset_selector.configs.directories import Directories


def init_logger(
    run_in_debug_mode: bool = False,
    folder_to_log_to: Path = Directories().LOGGING_FOLDER,
    write_log_files: bool = False,
) -> logging.Logger:
    """Set up logger either in default or debug mode.

    Outputs are written to a log folder with a date stamp.
    """
    # Defining what should be written to log.
    log_format = (
        "%(asctime)s - "
        "%(name)s - "
        "%(funcName)s - "
        "%(levelname)s - "
        "%(message)s"
    )

    # Defining colors e.g. red for error and yellow for warning.
    bold_seq = "\033[1m"
    colorlog_format = f"{bold_seq} " "%(log_color)s " f"{log_format}"
    colorlog.basicConfig(format=colorlog_format)

    logger = logging.getLogger(__name__)

    # If running in debug mode, we should be able to see debug
    # statements. Otherwise the lowest level of resolution is "info".
    if run_in_debug_mode:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # If there is no folder for logs, one should be created.
    if write_log_files:
        if not os.path.exists(folder_to_log_to):
            os.mkdir(folder_to_log_to)

        # Output the full log to a folder suffixed with the date.
        fh = logging.FileHandler(
            folder_to_log_to.joinpath(
                f"log_{str(datetime.datetime.today()).split()[0]}.log"
            )
        )
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter(log_format)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger


def row_checker(f):
    """Decorator for warning if the # of rows changes at input/output of a function."""
    logger = init_logger()

    @functools.wraps(f)
    def g(*args, **kwargs):
        # Assume first element parsed is the DF to monitor.
        if args:
            for elem in args:
                if isinstance(elem, pd.DataFrame):
                    # Assume first passed DataFrame is the one we monitor.
                    number_rows = len(elem)
                    break
        else:
            # To only loop once.
            for key, value in kwargs.items():
                if isinstance(value, pd.DataFrame):
                    # Assume first passed DataFrame is the one we monitor.
                    number_rows = len(value)
                    break

        result = f(*args, **kwargs)
        new_number_rows = len(result)

        if number_rows != new_number_rows:
            logger.warning(
                f"Number of rows has changed from "
                f"{number_rows} to {new_number_rows}"
            )
        return result

    return g


def logged(f):
    """Decorator for logging function execution (start and finish)."""
    module_logger = logging.getLogger(f.__module__)

    @functools.wraps(f)
    def g(*args, **kwargs):
        module_logger.info(f"Started {f.__name__}")
        ts = time.time()
        result = f(*args, **kwargs)
        te = time.time()
        module_logger.info(f"Finished {f.__name__} in {int((te - ts) * 1000) /1000}s")
        return result

    return g


def clean_string(string: str) -> str:
    """Make column names lower case.

    Replace spaces in column names with underscore
    Remove any special characters.
    """
    lower_case_and_no_spaces = re.sub(
        "[':;,&%€#\"()¿?$¢‰˜/]",
        "",
        string.lower()
        .replace(" ", "_")
        .replace("\u2013", "-")
        .replace("-", "_")
        .replace(".", "_")
        .replace("]", "_")
        .replace("[", "_")
        .replace("/", "_")
        .replace("\r\n", "_")
        .replace("\n", "_")
        .replace("\xa0", "_")
        .rstrip("_"),
    )
    while "__" in lower_case_and_no_spaces:
        lower_case_and_no_spaces = lower_case_and_no_spaces.replace("__", "_")

    return lower_case_and_no_spaces


def make_column_names_lower_case_and_no_spaces(df_or_list_or_str):
    """Function for making column names consistent.

    Should always be applied just after the loading of data.

    :param df_or_list_or_str: Can be a dataframe, list of string
    :return: Dataframe, list or string with changed column names
    """
    if type(df_or_list_or_str) not in (pd.DataFrame, list, str):
        return ValueError("Input not DataFrame, list or string")

    if isinstance(df_or_list_or_str, pd.DataFrame):
        df = df_or_list_or_str
        df.columns = [clean_string(col) for col in df.columns]
        return df

    elif isinstance(df_or_list_or_str, list):
        list_with_lower_case_and_no_spaces = [
            clean_string(x) for x in df_or_list_or_str
        ]
        return list_with_lower_case_and_no_spaces

    elif isinstance(df_or_list_or_str, str):
        return clean_string(df_or_list_or_str)
