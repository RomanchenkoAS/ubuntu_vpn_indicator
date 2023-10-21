from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon, QAction
import sys
import random # TODO to be removed


class TrayApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.tray_icon = QSystemTrayIcon(self.app)
        self.tray_menu = QMenu()

        print("Adding quit action")
        quit_action = QAction("Quit")
        quit_action.triggered.connect(self.quit_app)
        self.tray_menu.addAction(quit_action)

        print("Setting context menu")
        self.tray_icon.setContextMenu(self.tray_menu)

        print("Displaying icon")
        self.update_icon(self.status())

        # Set up a QTimer to run the `status` function periodically
        self.timer = QTimer(self.app)
        self.timer.timeout.connect(self.update_status)
        self.timer.start(5000)  # Run every 5000ms or 5 seconds

        self.tray_icon.show()

    def run(self):
        print("Entering event loop")
        sys.exit(self.app.exec())

    def quit_app(self):
        print("Quitting application")
        self.app.quit()

    def status(self):
        return random.choice(["on", "off", "disabled"])

    def update_status(self):
        new_status = self.status()
        print(f"Updating status to: {new_status}")
        self.update_icon(new_status)

    def update_icon(self, status):
        icon_paths = {
            "on": "icon/on.png",
            "off": "icon/off.png",
            "disabled": "icon/disabled.png"
        }
        icon = QIcon(icon_paths.get(status, "disabled"))
        if icon.isNull():
            print(f"Warning: Icon for status {status} is null!")
        self.tray_icon.setIcon(icon)
