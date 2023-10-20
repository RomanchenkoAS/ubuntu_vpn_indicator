import gi
import time
from threading import Thread

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

class TrayIndicator:
    def __init__(self):
        self.status_icon = Gtk.StatusIcon()
        self.update_icon("green")

    def update_icon(self, color):
        if color == "green":
            self.status_icon.set_from_icon_name("indicator-messages")
        elif color == "blue":
            self.status_icon.set_from_icon_name("indicator-keyboard")
        else:
            self.status_icon.set_from_icon_name("indicator-sound")

    def run_command(self):
        while True:
            # Run your command here and capture the output
            # Depending on the output, call self.update_icon("green") or self.update_icon("blue") etc.
            # For demo purposes, we're just toggling colors
            colors = ["green", "blue", "white"]
            for color in colors:
                GLib.idle_add(self.update_icon, color)
                time.sleep(1)
            time.sleep(1)

def main():
    indicator = TrayIndicator()
    thread = Thread(target=indicator.run_command)
    thread.daemon = True
    thread.start()
    Gtk.main()

if __name__ == "__main__":
    main()
