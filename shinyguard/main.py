import datetime
from dataclasses import dataclass
from typing import Union

from .network import get_ota_date_and_version, get_patch_commit_id_date, get_patch_date
from .utils import process_date

Date = Union[datetime.date, str]


@dataclass
class UpdateState:
    has_update: bool
    patch_date: datetime.date
    build_date: datetime.date
    version: str


def check_for_updates(*, build_date: Date, patch_date: Date, device: str) -> UpdateState:
    build_date = process_date(build_date)
    patch_date = process_date(patch_date)

    new_build_date, new_version = get_ota_date_and_version(device)
    commit_id, commit_date = get_patch_commit_id_date(new_version)
    new_patch_date = get_patch_date(commit_id)

    has_update = all((new_build_date > build_date, new_build_date > commit_date, new_patch_date > patch_date))

    return UpdateState(
        has_update=has_update, patch_date=new_patch_date.date(), build_date=new_build_date.date(), version=new_version
    )
