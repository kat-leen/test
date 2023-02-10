from source import func  # local packages


def test_get_date() -> None:
    """
    Check the date format.

    :return: None
    """

    date = func.get_date()
    date_split = date.split("-")

    assert len(date) == 10
    assert len(date_split) == 3

