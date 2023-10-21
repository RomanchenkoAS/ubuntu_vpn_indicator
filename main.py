from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QAction
import sys

class TrayApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        
        self.tray_icon = QSystemTrayIcon(self.app)
        
        # Create a menu for the tray icon
        self.tray_menu = QMenu()
        
        # Add a quit action to the menu
        quit_action = QAction("Quit")
        quit_action.triggered.connect(self.quit_app)
        self.tray_menu.addAction(quit_action)
        
        self.tray_icon.setContextMenu(self.tray_menu)
        
        # Set an icon for the tray (using a built-in icon as an example)
        self.tray_icon.setIcon(QIcon.fromTheme("dialog-information"))

        # Display the tray icon
        self.tray_icon.show()

    def run(self):
        sys.exit(self.app.exec())

    def quit_app(self):
        self.app.quit()


if __name__ == "__main__":
    tray_app = TrayApp()
    tray_app.run()
