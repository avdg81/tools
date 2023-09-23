import os
import unittest

import show_path as module_under_test


class TestShowPath(unittest.TestCase):
    def test_get_all_locations_if_none_is_empty(self):
        locations = ["/home", "/usr/bin", "/etc"]
        path = os.pathsep.join(locations)
        self.assertEqual(module_under_test.nonempty_locations_from(path), locations)

    def test_discard_empty_locations_from_path(self):
        locations = ["/home", "", "/usr/bin", ""]
        path = os.pathsep.join(locations)
        self.assertEqual(
            module_under_test.nonempty_locations_from(path),
            [locations[0], locations[2]],
        )


if __name__ == "__main__":
    unittest.main()
