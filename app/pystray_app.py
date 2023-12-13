import pystray
from pystray import MenuItem as item
from PIL import Image
from get_status import get_status
import time
import threading


class TrayApp:
    def __init__(self):
        self.icon = pystray.Icon("test_icon")
        self.icon.menu = pystray.Menu(
            item("Check Now", self.on_check),
            item("Quit", self.exit_action)
        )
        self.icon.run(self.setup)

    def create_icon(self, image_path):
        return Image.open(image_path)

    def on_check(self, icon, item):
        # print("ok")
        pass

    def exit_action(self, icon, item):
        icon.stop()
        # print("Quitting application")

    def setup(self, icon):
        self.update_icon("disabled")  # Set initial icon
        icon.visible = True
        threading.Thread(target=self.run_timer).start()

    def run_timer(self):
        while True:
            time.sleep(5)  # Run every 5000ms or 5 seconds
            self.update_status()

    def update_status(self):
        new_status = self.get_status_code()
        # print(f"Updating status to: {new_status}")
        self.update_icon(new_status)

    def get_status_code(self):
        # Dummy function; replace this with your actual get_status function
        return "on"

    def update_icon(self, status):
        icon_paths = {
            "on": "icon/on.png",
            "off": "icon/off.png",
            "disabled": "icon/disabled.png"
        }
        self.icon.icon = self.create_icon(icon_paths.get(status, "icon/disabled.png"))
