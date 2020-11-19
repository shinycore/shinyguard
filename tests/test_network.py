from datetime import datetime

import pytest

from shinyguard.exceptions import InvalidVersionError, MissingDeviceError, MissingPatchDateError
from shinyguard.network import get_ota_date_and_version, get_patch_commit_id_date, get_patch_date
from tests import constants as c


def test_build_available():
    date, version = get_ota_date_and_version(c.DEVICE_SUPPORTED)
    assert type(date) == datetime and type(version) == str


def test_build_not_available():
    with pytest.raises(MissingDeviceError):
        get_ota_date_and_version(c.DEVICE_UNSUPPORTED)


def test_version_valid():
    id_, date = get_patch_commit_id_date(c.VERSION_VALID)
    assert type(id_) == str and type(date) == datetime


def test_version_invalid():
    with pytest.raises(InvalidVersionError):
        get_patch_commit_id_date(c.VERSION_INVALID)


def test_gerrit_change_with_patch_date():
    date = get_patch_date(c.CHANGE_WITH_PATCH)
    assert type(date) == datetime


def test_gerrit_change_without_patch_date():
    with pytest.raises(MissingPatchDateError):
        get_patch_date(c.CHANGE_WITHOUT_PATCH)
