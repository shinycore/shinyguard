#!/usr/bin/env bash

coverage run -m pytest tests
coverage html -d /tmp/coverage
