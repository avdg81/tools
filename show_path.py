#!/usr/bin/env python
import os
import sys
import argparse

# Can we print in color?
has_colorama = False
try:
    import colorama
    has_colorama = True
except ImportError:
    pass


def nonempty_locations_from(path):
    return [location for location in path.split(os.pathsep) if location]


def _print_location(location, is_dir, is_duplicate):
    prefix = "    "
    color = None
    if is_duplicate:
        prefix = "+   "
        if has_colorama:
            color = colorama.Fore.CYAN
    elif not is_dir:
        prefix = "X   "
        if has_colorama:
            color = colorama.Fore.RED

    if color:
        prefix = color + prefix

    print(prefix + location)


def _print_path(path):
    locations = nonempty_locations_from(path)

    # Initialize colorama for colored output
    if has_colorama:
        colorama.init(autoreset=True)

    # Ignore differences in case for Windows only
    ignore_case = sys.platform == 'win32'

    printed = set()
    for location in locations:
        is_dir = os.path.isdir(location)
        location_ = location.lower() if ignore_case else location
        is_duplicate = location_ in printed
        _print_location(location, is_dir, is_duplicate)
        printed.add(location_)


def _main():
    """Run the command-line interface."""
    desc = "Print the search path in a human-friendly format"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("path_name", nargs="?", default="PATH",
                        help="variable name of path to show " +
                             "(default: %(default)s)")
    args = parser.parse_args()

    path_name = args.path_name
    try:
        path = os.environ[path_name].strip()
        if path:
            _print_path(path)
        else:
            print(f"{path_name} is empty")
    except KeyError:
        print(f"{path_name} not set")


if __name__ == '__main__':
    _main()
