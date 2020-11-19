import tests.constants as c
from shinyguard import check_for_updates


def test_date_time():
    result = check_for_updates(device=c.DEVICE_SUPPORTED, build_date=c.DATETIME_OBJECT, patch_date=c.DATETIME_OBJECT)
    assert result.has_update is True


def test_date_without_time():
    result = check_for_updates(device=c.DEVICE_SUPPORTED, build_date=c.DATE_OBJECT, patch_date=c.DATE_OBJECT)
    assert result.has_update is True


def test_date_as_string():
    result = check_for_updates(device=c.DEVICE_SUPPORTED, build_date=c.DATE_STRING, patch_date=c.DATE_STRING)
    assert result.has_update is True
