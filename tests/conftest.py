from datetime import timedelta

import requests_cache


def pytest_configure(config):
    requests_cache.install_cache(cache_name=".cache", backend="sqlite", expire_after=timedelta(hours=24))
    print("Cache enabled")
