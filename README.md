# shinyguard

Check for LineageOS security updates

## Introduction

*Every month*, new security updates for Android are released. You can find current patch's version in system settings ("Android security patch level"). If it's not available, then you have a bigger problem than just a missing entry.

LineageOS is an Android-based operating system which, at the moment of writing, has new builds released *weekly*. This means some updates can be skipped if you're interested only in security updates. And this is why I've made this app.

An important thing to note is that a security patch version of 2020-11-05 does not mean upstream patches were merged at that day. What's more, sometimes you'll need to wait another week for OTA update to be generated for your device.

## Installation

Using Poetry:

```bash
(.venv) $ poetry install
```

## Development stuff

### Unit tests with coverage

```bash
$ ./coverage.sh
```

Test results are exported to `/tmp/coverage`.

### Code style enforcement

```bash
$ git config core.hooksPath .githooks
```

Incorrectly formatted code (`.py` files, snippets in README.md) cannot be committed.
