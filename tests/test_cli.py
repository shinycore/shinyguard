import os
import sys
from pathlib import Path

import pytest
from docopt import DocoptExit

import tests.constants as c
from shinyguard.cli import cli as _cli

AOSP_GETPROP_BINARY_PATH = Path(__file__).parent.joinpath("bin/aosp")
LINEAGEOS_GETPROP_BINARY_PATH = Path(__file__).parent.joinpath("bin/lineageos")


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


def test_update_available_auto(cli, monkeypatch):
    monkeypatch.setitem(os.environ, "PATH", os.environ["PATH"] + ":" + str(LINEAGEOS_GETPROP_BINARY_PATH))
    out = cli("-a")
    assert out.splitlines()[0][10:] == " security update is available:"


def test_auto_missing_property(cli, monkeypatch):
    monkeypatch.setitem(os.environ, "PATH", os.environ["PATH"] + ":" + str(AOSP_GETPROP_BINARY_PATH))
    out = cli("-a")
    assert out == "This operating system is unsupported"


def test_auto_missing_getprop(cli, monkeypatch):
    out = cli("-a")
    assert out == "This operating system is unsupported"


def test_mutually_exclusive_options(cli):
    with pytest.raises(DocoptExit):
        cli("-d", c.DEVICE_SUPPORTED, "-p", c.DATE_STRING, "-b", c.DATE_STRING, "-a")
