from datetime import date, datetime

# do not edit this unless absolutely necessary

_YEAR = 2020
_MONTH = 1
_DAY = 1

DEVICE_SUPPORTED = "coral"
DEVICE_UNSUPPORTED = "dream"

VERSION_VALID = "17.1"
VERSION_INVALID = "999.0"

CHANGE_WITH_PATCH = "LineageOS%2Fandroid_build~lineage-17.1~I22fe42aa77ffb92f8dababcaf9ca1c6893fad606"
CHANGE_WITHOUT_PATCH = "LineageOS%2Fandroid_build~lineage-17.1~I61530b6da06e0038970551aa4d12bce02007ae3c"

# do not edit this at all

DATETIME_OBJECT = datetime(_YEAR, _MONTH, _DAY)
DATE_OBJECT = date(_YEAR, _MONTH, _DAY)
DATE_STRING = f"{_YEAR:04}-{_MONTH:02}-{_DAY:02}"

DATE_STRING_FUTURE = f"{(_YEAR+1):04}-{_MONTH:02}-{_DAY:02}"
