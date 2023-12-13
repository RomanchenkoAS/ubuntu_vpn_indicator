import sys
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon, QAction

from .get_status import get_status
from .get_icon import get_icon_path

class TrayApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.tray_icon = QSystemTrayIcon(self.app)
        self.tray_menu = QMenu()

        menu = QMenu()
        check_action = menu.addAction("Check Now")
        # check_action.triggered.connect(lambda: print("ok"))
        quit_action = menu.addAction("Quit")
        # quit_action.triggered.connect(lambda: print("ok"))

        # print("Adding quit action")
        quit_action = QAction("Quit")
        quit_action.triggered.connect(self.quit_app)
        self.tray_menu.addAction(quit_action)

        # print("Setting context menu")
        self.tray_icon.setContextMenu(self.tray_menu)

        # print("Displaying icon")
        self.update_icon(self.status())

        # Set up a QTimer to run the `status` function periodically
        self.timer = QTimer(self.app)
        self.timer.timeout.connect(self.update_status)
        self.timer.start(5000)  # Run every 5000ms or 5 seconds

        self.tray_icon.show()

    def run(self):
        # print("Entering event loop")
        sys.exit(self.app.exec())

    def quit_app(self):
        # print("Quitting application")
        self.app.quit()

    @staticmethod
    def status() -> str:
        status_code: str = ""
        match get_status():
            case "Not Connected" | "Disconnected":
                status_code = "disabled"
            case "Connected":
                status_code = "on"
            case "Failed":
                status_code = "off"
            case _:
                status_code = "off"

        return status_code

    def update_status(self) -> None:
        new_status: str = self.status()
        # print(f"Updating status to: {new_status}")
        self.update_icon(new_status)

    def update_icon(self, status: str) -> None:
        icon_paths = {
            "on": get_icon_path("on.png"),
            "off": get_icon_path("off.png"),
            "disabled": get_icon_path("disabled.png"),
        }
        # print(f"{icon_paths=}")
        icon = QIcon(icon_paths.get(status, "disabled"))
        self.tray_icon.setIcon(icon)
