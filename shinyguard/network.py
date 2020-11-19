import urllib.parse
from datetime import datetime

import requests

from .exceptions import InvalidVersionError, MissingDeviceError
from .schema import GerritChangeSchema, OTAUpdateListSchema

LINEAGE_OTA_URL = "https://download.lineageos.org/api/v1/{}/nightly/changelog"
GERRIT_CHANGE_LIST_URL = "https://review.lineageos.org/changes/"

GERRIT_SECURITY_PATCH_QUERY = 'project:LineageOS/android_build branch:lineage-{} status:merged "security string"'


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


def get_patch_commit_id_date(version: str) -> tuple[str, datetime]:
    query = urllib.parse.urlencode(
        {"q": GERRIT_SECURITY_PATCH_QUERY.format(version)}, quote_via=urllib.parse.quote
    )  # gerrit requires "%20" instead of the "+"

    response = requests.get(GERRIT_CHANGE_LIST_URL, query)
    response.raise_for_status()
    response_text_stripped = response.text[5:]  # first 5 chars are added by gerrit to prevent cross-site attacks

    changes = GerritChangeSchema(many=True).loads(response_text_stripped)
    changes.sort(key=lambda c: c["submitted"], reverse=True)

    try:
        latest = changes[0]
        return latest["id"], latest["submitted"]
    except IndexError as e:
        raise InvalidVersionError() from e
