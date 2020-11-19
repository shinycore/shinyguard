from datetime import datetime

import requests

from .exceptions import MissingDeviceError
from .schema import OTAUpdateListSchema

LINEAGE_OTA_URL = "https://download.lineageos.org/api/v1/{}/nightly/changelog"


def get_ota_date_and_version(device: str) -> tuple[datetime, str]:
    response = requests.get(LINEAGE_OTA_URL.format(device))
    response.raise_for_status()

    updates = OTAUpdateListSchema().loads(response.text)
    updates.sort(key=lambda u: u["datetime"], reverse=True)

    try:
        latest = updates[0]
        return latest["datetime"], latest["version"]
    except IndexError as e:
        raise MissingDeviceError() from e
