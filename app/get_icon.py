import sys
import os


def get_icon_path(icon_name):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, 'app', 'icon', icon_name)
