import re


def regex_match(pattern, text, ignore_case=False):
    flags = re.IGNORECASE if ignore_case else 0
    return bool(re.search(pattern, text, flags=flags))
