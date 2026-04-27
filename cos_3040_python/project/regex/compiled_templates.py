"""Contains compiled regular expression patterns used for validation."""

import re

check_valid_name = re.compile(r"^[a-zA-Z\s]+$")
