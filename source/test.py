from typing import Union, Any  # standard library
from pathlib import Path
import pickle
from datetime import datetime


def get_date() -> str:
    """
    Get the current date formatted as YYYY-MM-DD.

    :return: the date
    """
    return datetime.today().strftime("%Y-%m-%d")


def load_pickle(filepath: Union[Path, str]) -> Any:
    """
    Load a pickled object.

    :param filepath: the filepath of the pickle object to load
    :return: the pickled object
    """

    with open(Path(filepath), "rb") as file:
        obj = pickle.load(file)
    return obj


def save_pickle(obj: Any, path: Union[Path, str], filename: str) -> None:
    """
    Save an object with pickle.

    :param obj: the object to pickle
    :param path: the path to save the object
    :param filename: the filename of the object to pickle
    :return: *None*
    """
    assert obj is not None

    with open(Path(path) / f"{get_date()}_{filename}.pkl", "wb") as file:
        pickle.dump(obj, file, pickle.HIGHEST_PROTOCOL)
