from shinyguard.network import SECURITY_PATCH_VERSION_PATTERN

valid_diff = """
-      PLATFORM_SECURITY_PATCH := 2020-08-05
+      PLATFORM_SECURITY_PATCH := 2020-09-05
"""

invalid_misaligned_diff = """
 + PLATFORM_SECURITY_PATCH := 2020-09-05
+ PLATFORM_SECURITY_PATCH := 2020-09-05 
"""

invalid_multiline_diff = """
+ PLATFORM_SECURITY_PATCH
:= 2020-09-05
"""


def test_valid_diff():
    assert sum(1 for _ in SECURITY_PATCH_VERSION_PATTERN.finditer(valid_diff)) == 1


def test_invalid_misaligned_diff():
    assert sum(1 for _ in SECURITY_PATCH_VERSION_PATTERN.finditer(invalid_misaligned_diff)) == 0


def test_invalid_multiline_diff():
    assert sum(1 for _ in SECURITY_PATCH_VERSION_PATTERN.finditer(invalid_multiline_diff)) == 0
