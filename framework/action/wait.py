from framework.base_test import BaseTest


def wait_visible(element, timeout=15):
    BaseTest().wait(element, timeout=timeout)

