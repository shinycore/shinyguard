import sys

import pytest

import tests.constants as c
from shinyguard.cli import cli as _cli


@pytest.fixture
def cli(capsys, monkeypatch):
    def _cli_patched(*args: str) -> str:
        monkeypatch.setattr(sys, "argv", ("", *args))

        _cli()

        stdout, _ = capsys.readouterr()
        return stdout.strip()

    return _cli_patched


def test_update_available(cli):
    out = cli("-d", c.DEVICE_SUPPORTED, "-p", c.DATE_STRING, "-b", c.DATE_STRING)
    assert out.splitlines()[0][10:] == " security update is available:"


def test_no_updates(cli):
    out = cli("-d", c.DEVICE_SUPPORTED, "-p", c.DATE_STRING, "-b", c.DATE_STRING_FUTURE)
    assert out == "No new security updates"


def test_error_handling(cli):
    out = cli("-d", c.DEVICE_UNSUPPORTED, "-p", c.DATE_STRING, "-b", c.DATE_STRING)
    assert out == "No compatible builds found for the device"
