from source import test  # local packages


def test_get_date() -> None:
    """
    Check the date format.

    :return: None
    """

    date = test.get_date()
    date_split = date.split("-")

    assert len(date) == 10
    assert len(date_split) == 3

