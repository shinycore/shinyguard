"""Usage:
  shinyguard -d DEVICE -p DATE -b DATE

Options:
  -h --help                  Show this screen
  -d DEVICE --device=DEVICE  Device codename used by LineageOS
  -p DATE --patch-date=DATE  Currently installed security patch (YYYY-MM-DD format)
  -b DATE --build-date=DATE  Currently installed build (YYYY-MM-DD format)

These values can be found in Settings > System > About phone > Android version
"""

from docopt import docopt

from . import check_for_updates
from .exceptions import CheckError


def cli():
    args = docopt(__doc__)

    try:
        state = check_for_updates(
            device=args["--device"], patch_date=args["--patch-date"], build_date=args["--build-date"]
        )
    except CheckError as e:
        print(e)
        return

    if state.has_update:
        print(f"{state.patch_date} security update is available:")
        print(f"  - LineageOS version: {state.version}")
        print(f"  - Built on {state.build_date}")
    else:
        print("No new security updates")


if __name__ == "__main__":
    cli()  # pragma: no cover
