import re
import subprocess

SECURITY_PATCH_PROP = "ro.build.version.security_patch"
LINEAGE_VERSION_PROP = "ro.lineage.version"

LINEAGE_VERSION_PATTERN = re.compile(r".*-(?P<y>\d{4})(?P<m>\d{2})(?P<d>\d{2})-.*-(?P<device>\w+)")


class UnsupportedOSError(OSError):
    def __init__(self) -> None:
        super().__init__("This operating system is unsupported")


def getprop(name: str) -> str:
    try:
        process = subprocess.run(("getprop", name), stdout=subprocess.PIPE, encoding="utf-8")
    except FileNotFoundError as e:
        raise UnsupportedOSError() from e
    else:
        return process.stdout.strip()


def get_properties() -> dict:
    security_patch_str = getprop(SECURITY_PATCH_PROP)
    lineageos_version_str = getprop(LINEAGE_VERSION_PROP)

    lineageos_version_match = LINEAGE_VERSION_PATTERN.fullmatch(lineageos_version_str)
    if not lineageos_version_match:
        raise UnsupportedOSError()

    return dict(
        device=lineageos_version_match.group("device"),
        build_date="-".join(lineageos_version_match.group("y", "m", "d")),
        patch_date=security_patch_str,
    )
