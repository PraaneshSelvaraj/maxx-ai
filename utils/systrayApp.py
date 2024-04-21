from PySide2 import QtWidgets, QtGui
import sys

class SystemTrayApp(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent, awake):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip("Maxx-AI")
        self.awake = awake

        menu = QtWidgets.QMenu(parent)
        awake_opt = menu.addAction("Awake")
        awake_opt.triggered.connect(self.awake)
        awake_opt.setIcon(QtGui.QIcon("assets/images/icon.png"))
        menu.addSeparator()

        exit_opt = menu.addAction("Exit")
        exit_opt.triggered.connect(lambda: sys.exit())

        self.setContextMenu(menu)
        self.activated.connect(self.on_tray_icon_activated)

    def on_tray_icon_activated(self, reason):
        if reason == self.Trigger:
            self.awake()

class SystemTrayRunner():
    def __init__(self, awake):
        self.awake = awake

    def run(self):
        app=QtWidgets.QApplication(sys.argv)
        w=QtWidgets.QWidget()
        tray_icon=SystemTrayApp(QtGui.QIcon("assets/images/icon.png"),w, self.awake)
        tray_icon.show()
        sys.exit(app.exec_())